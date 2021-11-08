package com.ss.jb.assessmentOne;

import java.sql.Connection;
import java.math.BigDecimal;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;

public class SampleSingleton {

	private static Connection conn = null;
	private static SampleSingleton instance = null;
	
	
	public static SampleSingleton getInstance() {
		if(instance == null) {
			synchronized(instance) {
				instance = new SampleSingleton();
			}
		}
		return instance;
	}
	
	// Establishing DB Connection
	private SampleSingleton() {
		try{
			conn = DriverManager.getConnection("path","username","password");
		} catch (Exception e) {
			System.out.print("Error connecting to DB");
		}
	}
	
	
}
