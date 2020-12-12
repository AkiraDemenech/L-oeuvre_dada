import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Random;

public class Hexa {
	
	public static final int DIM = 4;
	
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
			
			for(String s : txt) {
				
				boolean b = true;
				String p = ".;!?";
				StringBuffer sb = new StringBuffer();
				for(int c=0; c<s.length(); c++) {
					
					s = s.toLowerCase();
					if(b)
						s = s.toUpperCase();
					
					if(p.indexOf(s.charAt(c))>=0)
						b = true;
					
					sb.append(s.charAt(c));
				
					if(Character.isLetterOrDigit(s.charAt(c)))
						b = false;
				}
				
				writer.write(sb.toString() + System.lineSeparator());
			}
			
			writer.close();
			
		} catch (IOException e) {
			return;
		}
		
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
	
	public static void juntar (List<String> l1, List<String> l2) {
		
		l1.add("-");
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
			for(String w : separe(s, " 	\n\r"))
				words.add(w);
		
		if(words.size()==0)
			return "";
			
		return words.get(random(words.size()));
	}
	
	public static Random r = new Random();
	
	public static List<String> make (List<String> poema) {
		
		List<String> p = new ArrayList<>();
		StringBuffer b;
		
		for(int c=0; c<poema.size(); c++) {
			
			b = new StringBuffer();
			while(b.length()<poema.get(c).length()) {
				String ss = random(poema);
				b.append(ss + " ");
				if(b.length()>=(poema.get(c).length()*(0.9)))
					break;
			}
				
			p.add(b.toString());
			
		}
		
		return p;
		
	}
	
	public static List<String> make (List<String> p, int v) {
		
		for(int c=0; c<v; c++)
			p = make(p);
		
		return p;
	}
	
	public static void seminario (Integer a) {
		if(a!=null)
		 System.out.println(a.toString());
	}
	
	public static void main (String[] args) {
		
		seminario(null);
		System.out.print("	GERANDO");
		
		List<String> poem = new ArrayList<>();
		List<String> base;
		
		for(int c=1; c<=DIM; c++) {
			
			System.out.print('.');
			base = read("Poema" + c + ".txt");
			juntar(poem, base);
			
			for(int i=2; i<=DIM; i++) {
				base = make(base, c);
				juntar(poem, base);
			}
			
			poem.add("=");
			
		}
		
		System.out.print("\n	OBRA ");
		write("New_Poem.txt", poem);
		for(int c = 0; c < DIM; c++) {
			if(c > 0)
				System.out.print(" × ");
			System.out.print(DIM);
		}
		
	}

}
