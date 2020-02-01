import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.text.DecimalFormat;
import java.util.Scanner;
import java.util.ArrayList;
import java.io.BufferedWriter;

public class MatrixMultiplication
{
	private static String PATH = "";
	private static int matrixSize = 0;
	private static double timeExec_exemplaires = 0.0;
	private static int matrixRes[][] = new int[matrixSize][matrixSize];

	public static void main(String[] args) throws InterruptedException, FileNotFoundException, IOException
	{
		try
		{
			String genTable = args[0];
			if(genTable.equals("genTable"))
			{
				PATH = args[1];
				String multType = args[2];

				avrgTimeExec(PATH, multType);
			}
			else
			{
				String pathA = args[0];
				String pathB = args[1];

				conventionalMultiplication(pathA, pathB);
			}
		}
		catch(Exception e)
		{
			System.out.println("Erreur : " + e);
		}
	}

	public static boolean validateFiles(String pathA, String pathB)
	{
		return existFile(pathA) && existFile(pathB);
	}

	public static boolean existFile(String path)
	{
		File file = new File(PATH + "/" + path);

		if(file.exists())
			return true;
		else
		{
			System.out.println("Fichier <" + path + "> n'existe pas!!!!!!!!");
			return false;
		}
	}

	public static boolean validateDimension(String pathA, String pathB) throws FileNotFoundException
	{
		int dimA = getDimension(pathA);
		int dimB = getDimension(pathB);

		if(dimA == dimB)
		{
			matrixSize = (int) Math.pow(2, dimA);
			return true;
		}
		else
		{
			System.out.println("dimension <" + dimB + "> incorrectee!!!!!!!!");
			return false;
		}
	}

	public static int getDimension(String fileName) throws FileNotFoundException
	{
		File file = new File(PATH + fileName);
		Scanner scanner = new Scanner(file);
		int dimension = 0;
		dimension = Integer.parseInt(scanner.nextLine());
		scanner.close();

		return dimension;
	}

	public static void conventionalMultiplication(String pathA, String pathB) throws FileNotFoundException, IOException
	{
		if(validateFiles(pathA, pathB) && validateDimension(pathA, pathB))
		{
			int matrix_A[][] = buildMatrix(pathA);
			int matrix_B[][] = buildMatrix(pathB);

			matrixRes = answerConvMulti(matrix_A, matrix_B);
			displayMatrix(matrixRes);
		}
	}

	public static int[][] buildMatrix(String path) throws FileNotFoundException
	{
		File file = new File(path);
		Scanner scanner = new Scanner(file);
		int lineNumber = 0;
		int currentMatrix[][] = new int[matrixSize][matrixSize];
		String matrixLine[] = new String[matrixSize];

		while (scanner.hasNextLine() != false)
		{
			lineNumber++;
			String currentLine = scanner.nextLine();
			if(lineNumber > 1)
			{
				matrixLine = currentLine.split("\t");
				for(int j =0; j<matrixSize; j++)
				{
					currentMatrix[lineNumber-2][j] = Integer.parseInt(matrixLine[j]);
				}
			}
		}
		scanner.close();

		return currentMatrix;
	}

	public static int[][] answerConvMulti(int[][] matrix_A, int[][] matrix_B) throws IOException
	{
		double startTime = System.nanoTime();
		int newMatrix[][]=new int[matrixSize][matrixSize];

		for(int i = 0; i < matrixSize; i++)
		{
			for(int j = 0; j < matrixSize; j++)
			{
				newMatrix[i][j]=0;
				for(int k = 0; k < matrixSize; k++)
				{
					newMatrix[i][j] += matrix_A[i][k] * matrix_B[k][j];
				}
			}
		}

		double endTime = System.nanoTime();
		double timeElapsed = endTime - startTime;

		System.out.println("Le temps d'execution en nanosecondes: " + timeElapsed);
		System.out.println("Le temps d'exectuion en secondes: " + timeElapsed / 1000000000);
		System.out.println("Taille de la matrice: " + matrixSize + "x" + matrixSize);
		System.out.println("-----------------------------------");

		timeExec_exemplaires += timeElapsed/1000000000;

		return newMatrix;
	}

	public static void displayMatrix(int[][] matrix)
	{
		for(int i=0; i<matrixSize ; i++){
			for(int j =0; j<matrixSize; j++)
			{
				System.out.print(matrix[i][j] + "\t");
			}
			System.out.println();
		}
	}

	public static void avrgTimeExec(String path, String multType) throws IOException
	{
		ArrayList<String> exemplaires = getExemplaires(path);
		ArrayList<Integer> dimensions = getListDimensions(exemplaires);

		if(!exemplaires.isEmpty() && !dimensions.isEmpty())
		{
			deleteFile("data.txt");
			getSameExemplaires(exemplaires,dimensions, multType);
		}

	}

	public static void getSameExemplaires(ArrayList<String> listExemplaires, ArrayList<Integer> listOfDim, String multType) throws IOException
	{
		int index = 0;

		for(int d : listOfDim)
		{
			ArrayList<String> sameExemplaires = new ArrayList<String>();
			for (int i = index ; i < listExemplaires.size(); i++)
			{
				if (listExemplaires.get(i).contains("ex_" + d))
				{
					sameExemplaires.add(listExemplaires.get(i));
					index = i + 1;
				}
			}
			multTwoByTwo(sameExemplaires, multType);
		}
	}

	public static ArrayList<String> getExemplaires(String path)
	{
		File folder = new File(path);
		File[] listOfFiles = folder.listFiles();
		ArrayList<String> listExemplaires = new ArrayList<String>();

		for (int i = 0; i < listOfFiles.length; i++)
		{
			if (listOfFiles[i].isFile() && listOfFiles[i].getName().contains("ex_"))
				listExemplaires.add(listOfFiles[i].getName());
		}

		return listExemplaires;
	}

	public static ArrayList<Integer> getListDimensions(ArrayList<String> listExemplaires) throws FileNotFoundException
	{
		int dim = 0;
		ArrayList<Integer> listOfDim = new ArrayList<Integer>();

		for(String exem : listExemplaires)
		{
			dim = getDimension(exem);
			if(!listOfDim.contains(dim))
				listOfDim.add(dim);
		}

		return listOfDim;
	}

	public static void multTwoByTwo(ArrayList<String> sameExemplaires, String multType) throws IOException
	{

		for(int i=0; i<sameExemplaires.size() - 1; i++)
		{
			for(int j=i+1; j<sameExemplaires.size(); j++)
			{
				switch(multType)
				{
					case "conv" :
					{
						System.out.println(sameExemplaires.get(i) + ":" + sameExemplaires.get(j));
						conventionalMultiplication(sameExemplaires.get(i), sameExemplaires.get(j));
					}
					break;
					default : System.out.println("Le type de multiplication n'existe pas!");
				}
			}
		}
		getCoord();
		System.out.println("--------------finish serie---------------------");
	}

	public static void getCoord() throws IOException
	{
		double avrgTimeExec = timeExec_exemplaires/10;
		String x = String.valueOf(new DecimalFormat("0.00").format(Math.log10(matrixSize)));

		String y = String.valueOf(avrgTimeExec);
		String coord = x + " " + y + "\n";

		writeInFile("data.txt", coord);
		timeExec_exemplaires = 0.0;
	}

	public static void deleteFile(String FileName) throws IOException
	{
		File file = new File(FileName);
		if(file.exists())
		{
			if(file.delete())
				System.out.println("File deleted successfully");
      else
				System.out.println("Failed to delete the file");
		}
	}

	public static void writeInFile(String path, String content) throws IOException
	{
    BufferedWriter writer = new BufferedWriter(new FileWriter(path, true));
		writer.append(content);
    writer.close();
	}
}
