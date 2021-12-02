import java.util.*;
import java.io.*;

public class part2 {

	public static void main(String[] args) throws FileNotFoundException{
		String fname = args[0];
		File fo = new File(fname);
		Scanner scanner = new Scanner(fo);
		ArrayList<Integer> report = new ArrayList<Integer>();
		while(scanner.hasNextLine()){
			report.add(Integer.parseInt(scanner.nextLine()));
		}

		System.out.println(solve(report));
	}

	public static int solve(List<Integer> input){
		int count = 0;

		for (int i = 0; i < input.size() - 3; i++){
			int a = input.get(i) + input.get(i + 1) + input.get(i + 2);
			int b = input.get(i + 1) + input.get(i + 2) + input.get(i + 3);
			if(a < b)		
				count++;
		}
		
		return count;
	}
}
