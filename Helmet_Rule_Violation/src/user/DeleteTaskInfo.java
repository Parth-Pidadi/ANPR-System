/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package user;


import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.Statement;


/**
 *
 * @author DILIP
 */
public class DeleteTaskInfo
{
    public void getDeletedData()
    {
        boolean flag=false;
        try
        {
            Class.forName("com.mysql.jdbc.Driver").newInstance();
            Connection conn=DriverManager.getConnection("jdbc:mysql://localhost:3306/helmetruleviolation","root","root");
            Statement st=conn.createStatement();
            
             String query="Delete  from taskinfo" ;
             int x=st.executeUpdate(query);
             if(x>0)
             {
                 flag=true;
             }
             flag=false;
        }
        catch(Exception e)
        {
            System.out.println(e);
            flag=false;
            
        }
        
        
      
    }
}
