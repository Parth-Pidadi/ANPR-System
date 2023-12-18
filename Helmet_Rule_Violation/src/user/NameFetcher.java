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
 * @author welcome
 */
public class NameFetcher
{
     public String getData(String username)
    {
        String a="";
        try
        {
            
            Class.forName("com.mysql.jdbc.Driver").newInstance();
            Connection conn=DriverManager.getConnection("jdbc:mysql://localhost:3306/helmetruleviolation","root","root");
            Statement st=conn.createStatement();
            
            String query="select * from registrationinfo where user_name='"+username+"' ";
            
            ResultSet rs=st.executeQuery(query);
            if(rs.next())
            {
              
                a=rs.getString(2);
                
            }
            System.out.println("a is:"+a);
            conn.close();
            st.close();
        }
        catch(Exception ex)
        {
            System.out.println("Exception is: "+ex);
        }
        return a;
    }
}
