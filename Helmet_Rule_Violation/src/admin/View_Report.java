/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package admin;

import user.*;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;

/**
 *
 * @author welcome
 */
public class View_Report 
{
    public void getImage_Info(String username)
    {
        try
        {
            Class.forName("com.mysql.jdbc.Driver").newInstance();
            Connection conn=DriverManager.getConnection("jdbc:mysql://localhost:3306/helmetruleviolation","root","root");
            Statement st1=conn.createStatement();
            Statement st2=conn.createStatement();
            String query="select * from image_info where user_name='"+username+"'";
            ResultSet rs1=st1.executeQuery(query);
            ResultSet rs2=st2.executeQuery(query);
            
            int row=0;
            while(rs1.next())
            {
                row++;
            }
            int i=0;
            String data[][]=new String[row][3];
            while(rs2.next())
            {
                   username=rs2.getString(1);
                   data[i][0]=username;
                   String vehiclename=rs2.getString(3);
                   data[i][1]=vehiclename;
                   String datetime=rs2.getString(4);
                   data[i][2]=datetime;
                   
                   i++;
            }
           View_Report_Frame.data=data;
        }
        catch(Exception ex)
        {
            System.out.println("Exception is: "+ex);
        }
    }
}
