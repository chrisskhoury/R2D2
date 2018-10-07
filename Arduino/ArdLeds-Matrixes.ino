#include <FastLED.h>
#include "LedControlMS.h"
   
    #define LedPin   8
    #define NbLeds  52
    #define Mat1Data   4
    #define Mat1Clk    5
    #define Mat1Load   6
    #define Mat2Data   12
    #define Mat2Clk    11
    #define Mat2Load   10

    char mode;
    long current;

     const uint64_t Emojis[] = {
      0x0018244281996600 /*<3*/ , 0x00003c4200240000 /*:)*/,
      0x00423c0000240000 /*:(*/ , 0xff8181bd5a181818 /*_|_*/,
      0xaa00aaaaaaaaaa00 /*!*/ 

    };

    const uint64_t Loading[] = {
      0x0000ff0306ff0000, 0x0000ff060cff0000, 0x0000ff0c18ff0000, 0x0000ff1830ff0000,
      0x0000ff3060ff0000, 0x0000ff60c0ff0000, 0x0000ffc081ff0000

    };

    const uint64_t Sound[] = {
      0x000008dd56624200, 0x000008dd62220000, 0x002022d70c080800, 0x000020db04000000,
      0x000424db12121010, 0x000024db42400000, 0x00042ad910000000, 0x0004066d98080000,
      0x00202067940c0400, 0x000022d508000000, 0x80c0a09d06040400, 0x004060dd03010000,
      0x004060dd03010000,

    };

    const uint64_t Silent[] = {
      0x000000fd02000000,  0x000008f700000000, 0x000008d720000000,  0x000000ff00000000,
      0x000010ef00000000,  0x000000df20000000, 0x000002dd20000000,  0x000000ff00000000,
      0x000000fd02000000,  0x000008f700000000, 0x000008d720000000,  0x000000ff00000000,
      0x000010ef00000000,  0x000000df20000000, 0x000002dd20000000,  0x000000ff00000000,


    };

    const uint64_t DanceMoves[] = {
      0x22140a1c281c141c, 0x2214081c2a1c141c, 0x2214281c0a1c141c, 0x22142a1c081c141c,
      0x2814281c0a1c141c, 0x0a14081c2a1c141c, 0x0036081c2a1c141c, 0x2016281c0a1c141c

    };
    
    CRGB leds[NbLeds];
    LedControl lc1=LedControl(Mat1Data,Mat1Clk,Mat1Load, 1);
    LedControl lc2=LedControl(Mat2Data,Mat2Clk,Mat2Load, 1);

    void Read(){
  
    while(millis()-current<5){
    char received = (char)Serial.read();
    if(received=='1') mode = '1';
    if(received=='2') mode = '2'; 
    if(received=='3') mode = '3'; 
    if(received=='4') mode = '4';
    if(received=='5') mode = '5'; 
    }
    Serial.println(mode);
  }

    void Display(int Mat , uint64_t set, int Delay){

if(Mat==0){
  for (int i=0;i<8;i++){
      byte row = (set>>i*8) & 0xFF;
    for (int j = 0; j<8 ; j++){
      lc1.setLed(0,i,j,bitRead(row,j));
      delay(Delay);
      }
    }
}
    
if(Mat==1){
  for (int i=0;i<8;i++){
      byte row = (set>>i*8) & 0xFF;
    for (int j = 0; j<8 ; j++){
      lc2.setLed(0,i,j,bitRead(row,j));
      delay(Delay);
      }
    }
}

  }
    
 
    void SetMode(char mode){
      switch (mode){
        case '1': Happy() ; break;
        case '2': Danger(); break;
        case '3': Dance() ; break;
        case '4': Love()  ; break;
        case '5': Speak() ; break;
      }
    }

    void Dance(){
      if(random(3,5)%2==0){
        for(int i=0 ; i<NbLeds;i++){
          leds[i] = CRGB ( random(1,200) + 50, random(1,200) + 50, 0);
          FastLED.show();
          delay(40);  
          if(i%3==0){
             Display(0 , DanceMoves[rand()%(sizeof(DanceMoves)/8)] , 0);
             Display(1 , DanceMoves[rand()%(sizeof(DanceMoves)/8)] , 0);  
          }
        }
      }
      else{
        for(int i=0 ; i<NbLeds;i++){
          leds[i] = CRGB ( 0, random(1,200) + 50, random(1,200) + 50);
          FastLED.show(); 
          delay(40); 
          if(i%3==0){
             Display(0 , DanceMoves[rand()%(sizeof(DanceMoves)/8)] , 0);
             Display(1 , DanceMoves[rand()%(sizeof(DanceMoves)/8)] , 0);  
          }
        }
      }
      
    }

    void Speak(){
      Display(0 , Sound[rand()%(sizeof(Sound)/8)] , 0);
      Display(1 , Sound[rand()%(sizeof(Sound)/8)] , 0);
      delay(100);
      Display(0 , Sound[rand()%(sizeof(Sound)/8)] , 0);
      Display(1 , Sound[rand()%(sizeof(Sound)/8)] , 0);
    }

    void Danger(){
     
      Display(0 , Emojis[4] , 0);
      Display(1 , Emojis[4] , 0);
      for (int i = 0; i <NbLeds; i++) {
      leds[i] = CRGB ( 255, 0, 0);
      FastLED.show();
      }
      delay(500);
      lc1.clearDisplay(0);
      lc2.clearDisplay(0);
      for (int i = 0; i <NbLeds; i++) {
        leds[i] = CRGB::Black;
        FastLED.show();

      }
    }

    void Happy(){
     Display(0,Emojis[1],10); 
     Display(1,Emojis[1],10);
      
      for (int i = 4; i <NbLeds-4; i++) {          
          leds[i-4] = CRGB ( 0 , 20 , 80 );
          leds[i-3] = CRGB ( 0 , 30 , 120);
          leds[i-2] = CRGB ( 0 , 40 , 160);
          leds[i-1] = CRGB ( 0 , 50 , 200);
          leds[i]   = CRGB ( 0 , 0  , 250);
          leds[i+1] = CRGB ( 0 , 50 , 200);
          leds[i+2] = CRGB ( 0 , 40 , 160);
          leds[i+3] = CRGB ( 0 , 30 , 120);
          leds[i+4] = CRGB ( 0 , 20 , 80 );

          
          FastLED.show();
          delay(20);
    
    }
    
    
      lc1.clearDisplay(0);
      lc2.clearDisplay(0);
    }

    void Love(){
      Display(0 , Emojis[0] , 20);
      Display(1 , Emojis[0] , 20);

      for (int i = 0; i <NbLeds-1; i++) {
      leds[i] = CRGB ( 100+2*i, 0, 0);
      leds[i+1] = CRGB ( 255 , 0 , 0);
      FastLED.show();
      delay(20);
      }

      
      lc1.clearDisplay(0);
      lc2.clearDisplay(0);
    }

    void setup() {            
  
      FastLED.addLeds<WS2812, LedPin, GRB>(leds, NbLeds);
      lc1.shutdown(0,false);
      lc1.setIntensity(0,1);
      lc1.clearDisplay(0);
      lc1.clearAll();
      lc2.shutdown(0,false);
      lc2.setIntensity(0,1);
      lc2.clearDisplay(0);
      lc2.clearAll();

      Serial.begin(9600);

    }

    void loop() {

        current = millis();
        Read();
        SetMode(mode);
    }

