import java.util.*;
import java.io.*;

public class part1 {

	public static void main(String[] args) throws FileNotFoundException{
		String fname = args[0];
		File fo = new File(fname);
		Scanner scanner = new Scanner(fo);
		ArrayList<String> lines = new ArrayList<String>();
		while(scanner.hasNextLine()){
			lines.add(scanner.nextLine());
		}

		System.out.println(solve(lines));
	}

	public static int solve(List<String> input){
		HashMap<String, Integer> m = new HashMap<String, Integer>();
		m.put("forward", 0);
		m.put("up", 0);
		m.put("down", 0);

		for (String line : input){
			String[] l = line.split(" ");
			m.put(l[0], m.get(l[0]) + Integer.parseInt(l[1]));
		}

		return m.get("forward") * (m.get("down") - m.get("up"));
	}
}
