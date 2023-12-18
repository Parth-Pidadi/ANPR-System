/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package admin;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.Statement;

/**
 *
 * @author welcome
 */
public class EditProfile 
{
     public boolean doEdit(String registeras,String name,String mobile,String email,String username,String password,String alphanumbericid )
    {
        boolean flag=true;
        try
        {
             Class.forName("com.mysql.jdbc.Driver").newInstance();
            Connection conn=DriverManager.getConnection("jdbc:mysql://localhost:3306/helmetruleviolation","root","root");
            Statement st=conn.createStatement();
            
            String query="update registrationinfo set registrer_as='"+registeras+"',name='"+name+"',mobile_number='"+mobile+"',email_id='"+email+"',password='"+password+"' ,alphanumberic_id='"+alphanumbericid+"'where user_name='"+username+"'";
            
            int x=st.executeUpdate(query);
            if(x>0)
                flag=true;
            else
                flag=false;
        }
        catch(Exception ex)
        {
            System.out.println("Exception is: "+ex);
        }
        return flag;
    }
}
