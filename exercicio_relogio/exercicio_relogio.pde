
//raio um pouco menor que a largura completa
float raio = 0.45*width;
float n;
float corteMaior = raio*0.90;
float corteMenor = raio*0.80;
void setup() {
  
  size(1000,1000);
  raio=0.45*width;
  corteMaior = raio*0.90;
  corteMenor = raio*0.95;
  
}

void draw() {

  translate(width/2,height/2);
  desenharCirculo();
  ////desenharQuadradoCircunscrito();
  desenharCortes();
  desenhadoHoras();
  
  println(raio);

}
 
void desenharShapeMouse(){
   
  n=3+(20*mouseX/width);
  beginShape();
  for(int i=0;i<n;i++){
    float a = i*TWO_PI/n;
    vertex(raio*cos(a),raio*sin(a));
    println(cos(a)); 
  }
  endShape(CLOSE);

} 

void desenharCirculo(){

  
   beginShape();
  for(int i=0;i<1000;i++){
    float a = i*TWO_PI/1000;
    vertex(raio*cos(a),raio*sin(a));
     
  }
  endShape(CLOSE);
  
}

void desenharQuadradoCircunscrito(){
  
   
   beginShape();
  for(int i=0;i<4;i++){
    float a = i*TWO_PI/4;
    vertex(raio*cos(a),raio*sin(a));
 
  }
  endShape(CLOSE);
  
}

void desenharCortes(){
    
   for(int i=0;i<60;i++){
    float a = i*TWO_PI/60;
      //cortes menores 
      if(i%5!=0){
        beginShape();
        vertex(raio*cos(a),raio*sin(a));
        vertex(corteMenor*cos(a),corteMenor*sin(a));
        endShape(CLOSE);
      }
      //cortes maiores
      else{
        beginShape();
        vertex(raio*cos(a),raio*sin(a));
        vertex(corteMaior*cos(a),corteMaior*sin(a));
        endShape(CLOSE);
      }
  }
  
}

void desenhadoHoras(){

  float s = map(second(), 0, 60, 0, TWO_PI) - HALF_PI;  // Values from 0 - 59
  float m = map(minute() + norm(second(), 0, 60), 0, 60, 0, TWO_PI) - HALF_PI;  // Values from 0 - 59
  float h = map(hour() + norm(minute(), 0, 60), 0, 24, 0, TWO_PI * 2) - HALF_PI;    // Values from 0 - 23
  line(0, 0, raio*cos(s),raio*sin(s));
  line(0, 0, (raio*0.75)*cos(m),(raio*0.75)*sin(m));
  //As horas somam uma fração dos minutos para não acontecer saltos
  line(0, 0, (raio*0.50)*cos(h),(raio*0.50)*sin(h));
  //  line(0, 0, raio*cos(h*HALF_PI/24),raio*sin(h*HALF_PI/24));
  //line(h, 66, h, 100);
  println(m/60+h);
 
}
  

     
