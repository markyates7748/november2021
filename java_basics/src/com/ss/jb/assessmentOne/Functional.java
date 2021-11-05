package com.ss.jb.assessmentOne;

import java.util.ArrayList;
import java.util.List;

public class Functional {
	
	//Given list of non-negative integers, return integer list of rightmost digits using %
	public List rightDigit(List<Integer> originalList) {
		List<Integer> tempList = new ArrayList<>();
		originalList.forEach(num -> tempList.add(num % 10));
		return tempList;
	}
	
	//Given list of integers, return list where each integer is multiplied by 2
	public List doubling(List<Integer> originalList) {
		List<Integer> tempList = new ArrayList<>();
		originalList.forEach(num -> tempList.add(num * 2));
		return tempList;
	}
	
	//Given list of strings, return list where each string has all its 'x' removed
	public List noX(List<String> originalList) {
		List<String> tempList = new ArrayList<>();
		originalList.forEach(str -> {
				tempList.add(str.replaceAll("x", ""));
			});
		return tempList;
	}
	
}
