import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Random;

public class Geral {
	//	
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
				
				m.add(s);
			}
			
			br.close();
			
		} catch (IOException e) {
			write(arq, Arrays.asList(" "));
		}
		
	}
	
	public static List<String> read (String nome) {
		
		List<String> l = new ArrayList<>();
		read(nome, l);
		return l;
		
	}
	
	public static void write (String nome, List<String> txt) {
		
		try {
			
			BufferedWriter writer = new BufferedWriter(new FileWriter(nome));
			
			for(String s : txt)
				writer.write(s + System.lineSeparator());
			
			writer.close();
			
		} catch (IOException e) {
			return;
		}
		
	}
	
	public static List<String> separe (String general, String separator) {
		
		List<String> list = new ArrayList<>();
		if(general==null || separator==null)
			return list;
		
		StringBuffer buff = new StringBuffer();
		for(int c=0; c<general.length(); c++) {
			
			if(separator.indexOf(general.charAt(c))!=-1) {
				if(buff.length()>0) {
					list.add(buff.toString());
					buff = new StringBuffer();
				}
			} else
				buff.append(general.charAt(c));
			
		}
		if(buff.length()>0)
			list.add(buff.toString());
		
		return list;
	}
	
	public static int random (int max) {
		return r.nextInt(max);
	}
	
	public static String random (List<String> t) {
		
		if(t==null || t.isEmpty())
			return "";
		
		List<String> words = new ArrayList<>();
		
		for(String s : t)
			for(String w : separe(s, " 	"))
				words.add(w);
		
		if(words.size()==0)
			return "";
			
		return words.get(random(words.size()));
	}
	
	public static String poem;
	public static List<String> poema;
	public static Random r;
	public static void make () {
		List<String> p = new ArrayList<>();
		StringBuffer b;
		for(int c=0; c<poema.size(); c++) {
			b = new StringBuffer();
			while(b.length()<poema.get(c).length()) {
				String ss = random(((random(4)==0)?(read(poem)):(poema)));
				b.append(ss + " ");
				if(b.length()>=(poema.get(c).length()*(0.9)))
					break;
			}
			p.add(b.toString());	
		}
		poema = p;
	}
	public static void main (String[] args) {
		poem = "poema.txt";
		if(args.length!=0)
			poem = juntar(args);
		poema = read(poem);
		r = new Random();
		System.out.print("\n\n			Poema ");
		do {
			make();
			System.out.print("Dada");
		} while(random(1+random(11))>0);
		System.out.println("\n");
		print(poema);
		write("new " + poem, poema);
	}
	public static void print (List<String> a) {	
		for(String s : a) {
			System.out.print("		");
			boolean b = true;
			String p = ".;!?";
			for(int c=0; c<s.length(); c++) {
				s = s.toLowerCase();
				if(b)
					s = s.toUpperCase();
				if(p.indexOf(s.charAt(c))>=0)
					b = true;
				
				System.out.print(s.charAt(c));
			
				if(Character.isLetterOrDigit(s.charAt(c)))
					b = false;
				
			}
			
			System.out.print("\n");
			
		}
		
	}
	
	public static String juntar (String[] partes) {
		StringBuffer buff = new StringBuffer();
		for(int c=0; c<partes.length; c++) {
			buff.append(partes[c]);
			if(c<partes.length-1)
				buff.append(" ");
		}
		return buff.toString();
	}
	

}
