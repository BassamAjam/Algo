import java.io.FileNotFoundException;
import java.io.IOException;

public class Conventional {

	private int matrix[][] = new int[0][0];
	private int dimension = 0;
	private double timeExecution = 0;

	public Conventional(Matrix mA, Matrix mB) throws IOException {
		if (validateDimension(mA.getDim(), mB.getDim())) {
			this.matrix = new int[this.dimension][this.dimension];

			double startTime = System.nanoTime();
			multiplyMatrices(mA.matrix, mB.matrix);
			showTimeExecuted(startTime);

		}
	}

	public Conventional(int[][] R) {
		this.matrix = R;
		this.dimension = R.length;
	}

	public double getTimeExecution() {
		return this.timeExecution;
	}

	public int getDim() {
		return this.dimension;
	}

	/* Multiplier deux matrices selon l'algorithme conventionnel */
	public int[][] multiplyMatrices(int[][] mA, int[][] mB) throws IOException {

		// System.out.println("here");
		for (int i = 0; i < this.dimension; i++) {
			for (int j = 0; j < this.dimension; j++) {
				this.matrix[i][j] = 0;
				for (int k = 0; k < this.dimension; k++) {
					this.matrix[i][j] += mA[i][k] * mB[k][j];
				}
			}
		}

		return matrix;
	}

	/* Calculuer le temps d'execution */
	public void showTimeExecuted(double startTime){
		double endTime = System.nanoTime();
		double elapsedTime = endTime - startTime;

		this.timeExecution = elapsedTime / 1000000000; // en secondes

		System.out.println("Conv - Le temps d'execution en nanosecondes: " + elapsedTime);
		System.out.println("Conv - Le temps d'exectuion en secondes: " + this.timeExecution);
		System.out.println("Conv - Taille de la matrice: " + dimension + "x" + dimension);
		System.out.println("-----------------------------------");
	}

	/* Vérifier si les deux matrices ont la meme dimension */
	public boolean validateDimension(int dimA, int dimB) throws FileNotFoundException {

		if (dimA == dimB) {
			this.dimension = dimA;
			return true;
		} else {
			System.out.println("dimension <" + dimA + ":" + dimB + "> incorrectee!!!!!!!!");
			return false;
		}

	}

	/* Afficher la matrice */
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
