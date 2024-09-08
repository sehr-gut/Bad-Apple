import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.awt.Color;
import java.io.FileNotFoundException;
import javax.imageio.ImageIO;
import java.util.concurrent.TimeUnit;


public class printer{


   public static File[] listFiles(){
      File frameFolder = new File("../badAppleFrames");      
      File [] frames = frameFolder.listFiles();      
      return frames;                
   }
   // getting the files from the folder

   public static void pixelValues(File image) throws IOException{
      String res = "";
      BufferedImage img = ImageIO.read(image);
      for(int y = 0; y <img.getHeight(); y+= 10){
         for(int x = 0; x < img.getWidth(); x+= 5){
            int pixel = img.getRGB(x, y);
            if((pixel & 0xff )== 0) res += " ";//if black ang background(change to # if naka lightmode)
            else res += "#";//change to " " if naka lightmode
         }
         res += "\n";
      }
      System.out.print(res);
   }
   //converting to ascii pero simple lang instead atong naay interpolation

   public static void main(String[] args) throws IOException{
      File[] listOfFrames = listFiles();

      for(File x: listOfFrames){
         pixelValues(x);
         try {
           Thread.sleep(17);//to match the bad apple fps(dili ko sure if tama ba ni)
         } catch (InterruptedException e) {
           Thread.currentThread().interrupt();
         }
      }     
   }
   //driver main code
}