/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package user;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.ArrayList;

/**
 *
 * @author 4250
 */
public class Task_Info_Fetcher 
{
      public ArrayList getTaskData()
    {
        ArrayList data=new ArrayList();
         try
        {
            
            Class.forName("com.mysql.jdbc.Driver").newInstance();
            Connection conn=DriverManager.getConnection("jdbc:mysql://localhost:3306/helmetruleviolation","root","root");
            Statement st=conn.createStatement();
            
            String query="select * from taskinfo";
            
            ResultSet rs=st.executeQuery(query);
            if(rs.next())
            {
               data.add(rs.getString(1));
               data.add(rs.getString(2));
               data.add(rs.getString(3));
               
            }
                
            System.out.println("data is:"+data);
            conn.close();
            st.close();
        }
        catch(Exception ex)
        {
            System.out.println("Exception is: "+ex);
        }
        return data;
    }
}
