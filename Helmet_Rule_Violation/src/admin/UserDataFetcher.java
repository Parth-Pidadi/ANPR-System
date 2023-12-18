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
import java.util.ArrayList;

/**
 *
 * @author welcome
 */
public class UserDataFetcher
{
     public ArrayList getData(String name)
    {
        ArrayList a=new ArrayList();
        try
        {
            
            Class.forName("com.mysql.jdbc.Driver").newInstance();
            Connection conn=DriverManager.getConnection("jdbc:mysql://localhost:3306/helmetruleviolation","root","root");
            Statement st=conn.createStatement();
            
            String query="select * from registrationinfo where name='"+name+"' ";
            
            ResultSet rs=st.executeQuery(query);
            while(rs.next())
            {
               
                a.add(rs.getString(5));
                a.add(rs.getString(6));
                a.add(rs.getString(7));
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
