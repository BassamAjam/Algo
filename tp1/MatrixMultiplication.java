import java.io.FileNotFoundException;
import java.io.IOException;

public class MatrixMultiplication {
	public static void main(String[] args) throws InterruptedException, FileNotFoundException, IOException {
		try {
			String genTable = args[0];
			if (genTable.equals("avrgTimeExec")) {
				String path = args[1];
				String multType = args[2];

				int seuil = 16;
				Multiplications mult = new Multiplications(path, multType, seuil);
				mult.run();

			} else {
					String pathA = args[0];
					String pathB = args[1];
					String multType = args[2];

					Matrix matrix_A = new Matrix(pathA);
					Matrix matrix_B = new Matrix(pathB);


					switch(multType){
						case "conv": {
							Conventional conv = new Conventional(matrix_A, matrix_B);
							conv.displayMatrix();
							break;
						}
						case "strassen": {
							int seuil = 1;
							Strassen strass = new Strassen(matrix_A, matrix_B, seuil);
							strass.displayMatrix();
							break;
						}
						case "strassenSeuil": {
							int seuil = 16;
							Strassen strass = new Strassen(matrix_A, matrix_B, seuil);
							strass.displayMatrix();
							break;
						}
						default: {
							System.out.println("Mauvais type de multiplication");
							break;
						}
					}
			}
		} catch (Exception e) {
			System.out.println("Erreur : " + e);
		}
	}
}
