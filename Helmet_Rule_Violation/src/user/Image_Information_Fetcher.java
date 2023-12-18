/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package user;

import java.sql.Blob;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.ArrayList;

/**
 *
 * @author welcome
 */
public class Image_Information_Fetcher 
{
    public ArrayList getImageInfo(String name)
    {
        ArrayList data=new ArrayList();
        try
        {
            Class.forName("com.mysql.jdbc.Driver").newInstance();
            Connection conn=DriverManager.getConnection("jdbc:mysql://localhost:3306/helmetruleviolation","root","root");
            Statement st=conn.createStatement();
            
            String query="select * from image_info where user_name='"+name+"'";
            ResultSet rs=st.executeQuery(query);
            
            if(rs.next())
            {
                
                Blob b1 = rs.getBlob("image");
                byte barr1[]=b1.getBytes(1,(int)b1.length());
                data.add(barr1);
               
            }
        }
        catch(Exception ex)
        {
            System.out.println("Exception is: "+ex);
        }
        return data;
    }
}
