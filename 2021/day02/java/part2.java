import java.util.*;
import java.io.*;

public class part2 {

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
		m.put("depth", 0);

		for (String line : input){
			String[] l = line.split(" ");

			if("forward".equals(l[0]))
				m.put("depth", m.get("depth") + Integer.parseInt(l[1]) * (m.get("down") - m.get("up")));

			
			m.put(l[0], m.get(l[0]) + Integer.parseInt(l[1]));
		}

		return m.get("forward") * m.get("depth");
	}
}
