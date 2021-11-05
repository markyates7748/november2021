package com.ss.jb.assessmentOne;

import java.math.BigDecimal;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;

import java_basics_day_four.Singleton;


public class SampleSingleton {

	private static Connection conn = null;
	
	private static SampleSingleton instance = null;
	
	public static SampleSingleton getInstance() {
		if(instance == null) {
			synchronized(Singleton .class) {
				if(instance == null) {
					instance = new SampleSingleton();
				}
			}
		}
		return instance;
	}
	
}
