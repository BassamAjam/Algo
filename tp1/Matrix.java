import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Matrix {

	private File file = new File("");
	private String path = "";

	private int dimension = 0;
	public int matrix[][] = new int[0][0];

	Matrix(String path) throws FileNotFoundException {
		this.path = path;
		this.file = new File(this.path);
		this.dimension = this.getdimension();
		this.matrix = new int[this.dimension][this.dimension];

		if (this.dimension != 0)
			this.buildMatrix();
	}

	public int getDim() {
		return this.dimension;
	}

	public void setDim(int dimension) {
		this.dimension = dimension;
	}

	public boolean existFile(File file) {
		if (file.exists())
			return true;
		else {
			System.out.println("Fichier <" + this.path + "/" + path + "> n'existe pas!!!!!!!!");
			return false;
		}
	}

	public int getdimension() throws FileNotFoundException {

		return this.dimension = (int) Math.pow(2, getSize());

	}

	public int getSize() throws FileNotFoundException {
		if (!existFile(this.file)) {
			System.out.println("Fichier <" + this.path + "> n'existe pas!!!!!!!!");

			return 0;

		} else {
			return Integer.parseInt(new Scanner(this.file).nextLine());
		}
	}

	public int[][] buildMatrix() throws FileNotFoundException {
		Scanner scanner = new Scanner(this.file);
		int lineNumber = 0;
		String matrixLine[] = new String[this.dimension];

		while (scanner.hasNextLine() != false) {
			lineNumber++;
			String currentLine = scanner.nextLine();

			if (lineNumber > 1) {
				matrixLine = currentLine.split("\t");
				for (int j = 0; j < this.dimension; j++) {
					this.matrix[lineNumber - 2][j] = Integer.parseInt(matrixLine[j]);
				}
			}
		}
		scanner.close();

		return this.matrix;
	}

	public void displayMatrix() {
		for (int i = 0; i < this.dimension; i++) {
			for (int j = 0; j < this.dimension; j++) {
				System.out.print(this.matrix[i][j] + "\t");
			}
			System.out.println();
		}

		System.out.println("--------------------------------");
	}

}
