/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package admin;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;

/**
 *
 * @author welcome
 */
public class View_User_Profile 
{
  public static String registeras="User";
     public void getData()
    {
        
        try
        {
             Class.forName("com.mysql.jdbc.Driver").newInstance();
            Connection conn=DriverManager.getConnection("jdbc:mysql://localhost:3306/helmetruleviolation","root","root");
            Statement st1=conn.createStatement();
            Statement st2=conn.createStatement();
            
            String query="select * from registrationinfo where registrer_as='"+registeras+"'";
            
            ResultSet rs1=st1.executeQuery(query);
            ResultSet rs2=st2.executeQuery(query);
            
             int row=0;
            
            while(rs1.next())
            {
                row++;
            }
            
            int i=0;
             String[][] data=new String[row][3];
              while(rs2.next())
            {
                
               
                String name=rs2.getString(2);
                data[i][0]=name;
                String mobile=rs2.getString(3);
                data[i][1]=mobile;
                 String email=rs2.getString(4);
                data[i][2]=email;
                 
                i++;
            }
             View_User_Profile_Frame.data1=data;
            // System.out.println("Query is: "+query);
             
        }
        catch(Exception e)
        {
            System.out.println(e);
        }
    }
}
