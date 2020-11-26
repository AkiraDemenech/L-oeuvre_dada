import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Random;

public class Bingo {

public static void read (String arq, List<String> m) {
	
		if(m==null)
			return;
		
		BufferedReader br;
		
		try {
			
			br = new BufferedReader(new FileReader(arq));
		
			while(true) {
				
				String s = br.readLine();
				
				if(s==null)
					break;
				
				for(String p : separe(s.toUpperCase())) {
					
					boolean b = true;
					
					for(String o : m)
						if(o.equals(p))
							b = false;
					
					if(b)
						m.add(p);
				}
			}
			
			br.close();
			
		} catch (IOException e) {
			writer(arq, Arrays.asList(""));
		}
		
	}
	
	public static List<String> read (String nome) {
		
		List<String> l = new ArrayList<>();
		read(nome + ".txt", l);
		return l;
		
	}
	
	public static void write (String nome, List<String> txt) {
		
		int c = 1;
		try {
			
			while(true) {
				BufferedReader br = new BufferedReader(new FileReader(nome + "(" + c + ").txt"));
				c++;
				br.close();
			}
			
		} catch (IOException e) {
			nome = nome + "(" + c + ").txt";
		}
		
		writer(nome, txt);
		
	}
	
	public static void writer (String nome, List<String> txt) {
		
		try {
			
			BufferedWriter writer = new BufferedWriter(new FileWriter(nome));
			
			for(String s : txt)
				writer.write(s + System.lineSeparator());
			
			writer.close();
			
		} catch (IOException e) {
			return;
		}
		
	}
	
	public static void writes (String nome, List<List<String>> txt) {
		
		List<String> a = new ArrayList<>();
		for(List<String> l : txt) {
			juntar(a, l);
			a.add("");
		}
		
		write(nome, a);
		
	}
	
	public static List<String> separe (String general) {
		
		List<String> list = new ArrayList<>();
		if(general==null)
			return list;
		
		general = general.toUpperCase();
		
		StringBuffer buff = new StringBuffer();
		for(int c=0; c<general.length(); c++) {
			
			if(Character.isLetterOrDigit(general.charAt(c))) {
				if(Character.isLetter(general.charAt(c)))
					buff.append(general.charAt(c));
			} else if(buff.length()>0) {
				list.add(buff.toString());
				buff = new StringBuffer();
			}
			
		}
		if(buff.length()>0)
			list.add(buff.toString());
		
		return list;
	}
	
	public static void juntar (List<String> l1, List<String> l2) {
		
		for(String s : l2)
			l1.add(s);
		
	}
	
	public static int random (int max) {
		return r.nextInt(max);
	}
	
	public static String random (List<String> t) {
		
		if(t==null || t.isEmpty())
			return "";
		
		List<String> words = new ArrayList<>();
		
		for(String s : t)
			for(String w : separe(s))
				words.add(w);
		
		if(words.size()==0)
			return "";
		
		return words.remove(random(words.size()));
	}
	
	public static Random r;
	
	public static void main(String[] args) {
		
		r = new Random();
		String bingo = "bingo";
		String palavras = "palavras";
		String usadas = "as_palavras_usadas";
		List<String> words = read(palavras);
		int quant = 20;
		int cartela = 9;
		int repeat = 4;
		List<List<String>> cart = new ArrayList<>();
		List<String> uso = new ArrayList<>();
		
		if(args.length>0) {
			try {
				quant = Integer.parseInt(args[0]);
			} catch (NumberFormatException e) {
				quant = 20;
			}
		}
		
		writer(palavras+".txt", words);
		
		for(int c=0; c<quant; c++) {
			cart.add(new ArrayList<>());
			for(int i=0; i<cartela; i++)
				if(c>0 && i<=random(repeat))
					cart.get(c).add(cart.get(c-1).get(cartela-i-1));
				else {
					String s = random(words);
					cart.get(c).add(s);
					uso.add(s);
					System.out.print(s + " ");
				}
		}
		
		
		System.out.print("\n\n" + words.size());
		writes(bingo, cart);
		System.out.print(" > ");
		write(usadas, uso);
		System.out.println(uso.size());
		
	}

}
