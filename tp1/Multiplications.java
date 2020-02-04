import java.io.BufferedWriter;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.text.DecimalFormat;
import java.util.ArrayList;
import java.util.Scanner;

public class Multiplications {

	private File file = new File("");
	private String path = "";
	private String type = "";
	
	private double timeExecSerie = 0.0;
	
	private int dimension = 0;
	private int seuil = 0;

	Multiplications(String path, String type, int seuil) throws IOException {
		this.path = path;
		this.type = type;
		this.seuil = seuil;
		this.file = new File(this.path);

	}
	
	public void run() throws IOException {
		ArrayList<String> exemplaires = getExemplaires();
		ArrayList<Integer> dimensions = getListDimensions(exemplaires);

		if (!exemplaires.isEmpty() && !dimensions.isEmpty()) {
			deleteFile("data.txt");
			writeInFile("data.txt", this.type + " " + this.seuil + "\n" );
			getSameExemplaires(exemplaires, dimensions, this.type);
		}
	}

	public ArrayList<String> getExemplaires() {
		File[] listOfFiles = this.file.listFiles();
		ArrayList<String> listExemplaires = new ArrayList<String>();

		for (int i = 0; i < listOfFiles.length; i++) {
			if (listOfFiles[i].isFile() && listOfFiles[i].getName().contains("ex_"))
				listExemplaires.add(listOfFiles[i].getName());
		}
		
		return listExemplaires;
	}

	public ArrayList<Integer> getListDimensions(ArrayList<String> listExemplaires) throws FileNotFoundException {
		int dim = 0;
		ArrayList<Integer> listOfDim = new ArrayList<Integer>();

		for (String exem : listExemplaires) {
			dim = getSize(exem);
			if (!listOfDim.contains(dim))
				listOfDim.add(dim);
		}
		
		return listOfDim;
	}

	public int getSize(String exemplaire) throws FileNotFoundException {
		return Integer.parseInt(new Scanner(new File(this.path + "/" + exemplaire)).nextLine());
	}
	
	public void getSameExemplaires(ArrayList<String> listExemplaires, ArrayList<Integer> listOfDim,
			String multType) throws IOException {
		int index = 0;

		for (int d : listOfDim) {
			ArrayList<String> sameExemplaires = new ArrayList<String>();
			for (int i = index; i < listExemplaires.size(); i++) {
				if (listExemplaires.get(i).contains("ex_" + d)) {
					sameExemplaires.add(listExemplaires.get(i));
					index = i + 1;
				}
			}
			multTwoByTwo(sameExemplaires, multType);
		}
	}
	
	public void multTwoByTwo(ArrayList<String> sameExemplaires, String multType) throws IOException {

		for (int i = 0; i < sameExemplaires.size() - 1; i++) {
			for (int j = i + 1; j < sameExemplaires.size(); j++) {
				Matrix mA = new Matrix(this.path + "/" + sameExemplaires.get(i));
				Matrix mB = new Matrix(this.path + "/" + sameExemplaires.get(j));

				switch (multType) {
				case "conv": {
					System.out.println(sameExemplaires.get(i) + ":" + sameExemplaires.get(j));

					Conventional conv = new Conventional(mA, mB);
					this.timeExecSerie += conv.getTimeExecution();
					this.dimension = conv.getDim();
					// conv.displayMatrix();
					break;
				}
				case "strassen" :
				case "strassenSeuil": {
					System.out.println(sameExemplaires.get(i) + ":" + sameExemplaires.get(j));
					Strassen strass = new Strassen(mA, mB, this.seuil);
					this.timeExecSerie += strass.getTimeExecution();
					this.dimension = strass.getDim();
					// strass.displayMatrix();
					break;
				}
				default:
					System.out.println("Le type de multiplication n'existe pas!");
				}
			}
		}
		getCoord();
		System.out.println("--------------finish serie---------------------");
	}

	public void getCoord() throws IOException {
		double avrgTimeExec = this.timeExecSerie / 10;
		String x = String.valueOf(new DecimalFormat("0.0000").format(Math.log10(this.dimension)));
		String y = String.valueOf(avrgTimeExec);
		String coord = x + " " + y + "\n";

		writeInFile("data.txt", coord);
		this.timeExecSerie = 0.0;
		this.dimension = 0;
	}

	public void deleteFile(String FileName) throws IOException {
		File file = new File(FileName);
		if (file.exists()) {
			if (file.delete())
				System.out.println("File deleted successfully");
			else
				System.out.println("Failed to delete the file");
		}
	}

	public void writeInFile(String path, String content) throws IOException {
		BufferedWriter writer = new BufferedWriter(new FileWriter(path, true));
		writer.append(content);
		writer.close();
	}
}
