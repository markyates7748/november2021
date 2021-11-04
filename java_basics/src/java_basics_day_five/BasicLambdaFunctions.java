/**
 * 
 */
package java_basics_day_five;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.stream.Collectors;

/**
 * @author myate
 *
 */
public class BasicLambdaFunctions {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		List<String> simpleStringArray = new ArrayList<>();
		simpleStringArray.add("ate");
		simpleStringArray.add("Hello");
		simpleStringArray.add("this");
		simpleStringArray.add("is");
		simpleStringArray.add("Mark");
		simpleStringArray.add("Yates");
		simpleStringArray.add("with");
		simpleStringArray.add("a");
		simpleStringArray.add("simple");
		simpleStringArray.add("lambda");
		simpleStringArray.add("function");
		simpleStringArray.add("demo");
		simpleStringArray.add("program");
		simpleStringArray.add("ahk");
		simpleStringArray.add("ant");
		simpleStringArray.add("app");

		//No ordering
		System.out.println("Input order");
		simpleStringArray.forEach(System.out :: println);
		System.out.println();
		
		//Ordered by length s -> l
		System.out.println("Ordered by length");
		simpleStringArray.stream()
			.sorted(Comparator.comparing(String :: length))
			.collect(Collectors.toList())
			.forEach(System.out :: println);
		System.out.println();
		
		//Ordered by reverse length l -> s
		System.out.println("Ordered by reverse length");
		simpleStringArray.stream()
			.sorted(Comparator.comparing(String :: length, Comparator.reverseOrder()))
			.collect(Collectors.toList())
			.forEach(System.out :: println);
		System.out.println();
		
		//Ordered by first letter
		System.out.println("Ordered by first letter");
		simpleStringArray.stream()
			.sorted(Comparator.comparing(str -> str.charAt(0)))
			.collect(Collectors.toList())
			.forEach(System.out :: println);
		System.out.println();
		
		//Ordered by having 'e'
		System.out.println("Ordered by having 'e'");
		simpleStringArray.stream()
			.filter(str -> str.contains("e"))
			.forEach(System.out :: println);
		simpleStringArray.stream()
			.filter(str -> !str.contains("e"))
			.forEach(System.out :: println);
		System.out.println();
		
	}
	
}
