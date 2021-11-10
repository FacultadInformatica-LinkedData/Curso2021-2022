package main;

import javax.swing.GroupLayout.Alignment;
import javax.swing.GroupLayout;
import javax.swing.LayoutStyle.ComponentPlacement;
import javax.swing.JTextArea;
import javax.swing.JScrollPane;
import java.awt.Font;
import java.awt.Color;

public class Interfaz extends javax.swing.JFrame {

	String distrito;
	String barrio;

	/**
	 * Creates new form DisplayFrame
	 */
	public Interfaz() {
		initComponents();
		setLocationRelativeTo(null);
	}

	static App a = new App();

	/**
	 * This method is called from within the constructor to initialize the form.
	 * WARNING: Do NOT modify this code. The content of this method is always
	 * regenerated by the Form Editor.
	 */

	// <editor-fold defaultstate="collapsed" desc="Generated Code">
	private void initComponents() {

		jPanel1 = new javax.swing.JPanel();
		jButton1 = new javax.swing.JButton();
		ComboDistrito = new javax.swing.JComboBox<>();
		ComboBarrio = new javax.swing.JComboBox<>();
		LabelDistrito = new javax.swing.JLabel();
		LabelBarrio = new javax.swing.JLabel();
		PanelColor = new javax.swing.JPanel();
		LabelTitulo = new javax.swing.JLabel();

		setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);
		setBackground(new java.awt.Color(176, 224, 230));
		setCursor(new java.awt.Cursor(java.awt.Cursor.DEFAULT_CURSOR));
		setPreferredSize(new java.awt.Dimension(1000, 650));

		jPanel1.setBackground(new java.awt.Color(255, 255, 255));
		jPanel1.setPreferredSize(new java.awt.Dimension(1000, 650));

		jButton1.setBackground(new java.awt.Color(176, 224, 255));
		jButton1.setFont(new java.awt.Font("Century Gothic", 1, 18)); // NOI18N
		jButton1.setText("Buscar");
		jButton1.addActionListener(new java.awt.event.ActionListener() {
			public void actionPerformed(java.awt.event.ActionEvent evt) {
				buttonActionPerformed(evt);
			}
		});

		ComboDistrito.setBackground(new java.awt.Color(176, 224, 230));
		ComboDistrito.setFont(new java.awt.Font("Century Gothic", 0, 18)); // NOI18N
		ComboDistrito.setModel(new javax.swing.DefaultComboBoxModel<>(
				new String[] { "01-CENTRO", "02-ARGANZUELA", "03-RETIRO", "04-SALAMANCA", "05-CHAMARTIN", "06-TETUAN",
						"07-CHAMBERI", "08-FUENCARRAL-EL-PARDO", "09-MONCLOA-ARAVACA" }));

		ComboBarrio.setBackground(new java.awt.Color(176, 224, 230));
		ComboBarrio.setFont(new Font("Century Gothic", Font.PLAIN, 18)); // NOI18N
		ComboBarrio.setModel(new javax.swing.DefaultComboBoxModel<>(new String[] { "01-01-PALACIO", "01-02-EMBAJADORES",
				"01-03-CORTES", "01-04-JUSTICIA", "01-05-UNIVERSIDAD", "01-06-SOL", "02-01-IMPERIAL", "02-02-ACACIAS",
				"02-03-CHOPERA", "02-04-LEGAZPI", "02-05-DELICIAS", "02-06-PALOS-DE-MOGUER", "02-07-ATOCHA",
				"03-01-PACIFICO", "03-02-ADELFAS", "03-03-ESTRELLA", "03-04-IBIZA", "03-05-JERONIMOS",
				"03-06-NINIO-JESUS", "04-01-RECOLETOS", "04-02-GOYA", "04-03-FUENTE-DEL-BERRO", "04-04-GUINDALERA",
				"04-05-LISTA", "04-06-CASTELLANA", "05-01-EL-VISO", "05-02-PROSPERIDAD", "05-03-CIUDAD-JARDIN",
				"05-04-HISPANOAMERICA", "05-05-NUEVA-ESPANIA", "05-06-CASTILLA", "06-01-BELLAS-VISTAS",
				"06-02-CUATRO-CAMINOS", "06-03-CASTILLEJOS", "06-04-ALMENARA", "06-05-VALDEACEDERAS",
				"06-06-BERRUGUETE", "07-01-GAZTAMBIDE", "07-02-ARAPILES", "07-03-TRAFALGAR", "07-04-ALMAGRO",
				"07-05-RIOS-ROSAS", "07-06-VALLEHERMOSO", "08-04-EL-PILAR", "08-05-LA-PAZ", "09-01-CASA-DE-CAMPO",
				"09-02-ARGUELLES", "09-03-CIUDAD-UNIVERSITARIA", "09-04-VALDEZARZA" }));

		LabelDistrito.setFont(new java.awt.Font("Century Gothic", 0, 24)); // NOI18N
		LabelDistrito.setText("Elige un distrito:");
		// CampoResultados.setText(" ");

		LabelBarrio.setFont(new java.awt.Font("Century Gothic", 0, 24)); // NOI18N
		LabelBarrio.setText("Elige un barrio:");

		PanelColor.setBackground(new Color(204, 153, 255));

		LabelTitulo.setFont(new java.awt.Font("Century Gothic", 1, 36)); // NOI18N
		LabelTitulo.setText("Parquímetros de Madrid");

		javax.swing.GroupLayout PanelColorLayout = new javax.swing.GroupLayout(PanelColor);
		PanelColorLayout.setHorizontalGroup(
			PanelColorLayout.createParallelGroup(Alignment.LEADING)
				.addGroup(PanelColorLayout.createSequentialGroup()
					.addGap(227)
					.addComponent(LabelTitulo)
					.addContainerGap(262, Short.MAX_VALUE))
		);
		PanelColorLayout.setVerticalGroup(
			PanelColorLayout.createParallelGroup(Alignment.LEADING)
				.addGroup(PanelColorLayout.createSequentialGroup()
					.addGap(26)
					.addComponent(LabelTitulo)
					.addContainerGap(29, Short.MAX_VALUE))
		);
		PanelColor.setLayout(PanelColorLayout);

		scrollPane = new JScrollPane();

		// LabelResultados.setText(" ");

		javax.swing.GroupLayout jPanel1Layout = new javax.swing.GroupLayout(jPanel1);
		jPanel1Layout.setHorizontalGroup(jPanel1Layout.createParallelGroup(Alignment.LEADING).addGroup(jPanel1Layout
				.createSequentialGroup()
				.addGroup(jPanel1Layout.createParallelGroup(Alignment.LEADING, false).addGroup(jPanel1Layout
						.createSequentialGroup()
						.addGroup(jPanel1Layout.createParallelGroup(Alignment.LEADING).addGroup(jPanel1Layout
								.createSequentialGroup().addGap(60)
								.addGroup(jPanel1Layout.createParallelGroup(Alignment.LEADING)
										.addGroup(jPanel1Layout.createParallelGroup(Alignment.TRAILING, false)
												.addComponent(ComboBarrio, Alignment.LEADING, 0, 0, Short.MAX_VALUE)
												.addComponent(ComboDistrito, Alignment.LEADING, 0, 228, Short.MAX_VALUE)
												.addComponent(LabelDistrito, Alignment.LEADING))
										.addComponent(LabelBarrio)))
								.addGroup(jPanel1Layout.createSequentialGroup().addGap(109).addComponent(jButton1,
										GroupLayout.PREFERRED_SIZE, 124, GroupLayout.PREFERRED_SIZE)))
						.addGap(18).addComponent(scrollPane))
						.addGroup(jPanel1Layout.createSequentialGroup().addGap(32).addComponent(PanelColor,
								GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE)))
				.addGap(858)));
		jPanel1Layout.setVerticalGroup(jPanel1Layout.createParallelGroup(Alignment.LEADING).addGroup(jPanel1Layout
				.createSequentialGroup().addContainerGap()
				.addComponent(PanelColor, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE,
						GroupLayout.PREFERRED_SIZE)
				.addGroup(jPanel1Layout.createParallelGroup(Alignment.LEADING)
						.addGroup(jPanel1Layout.createSequentialGroup().addGap(235).addComponent(ComboBarrio,
								GroupLayout.PREFERRED_SIZE, 41, GroupLayout.PREFERRED_SIZE))
						.addGroup(jPanel1Layout.createSequentialGroup().addGap(43).addGroup(jPanel1Layout
								.createParallelGroup(Alignment.BASELINE)
								.addComponent(scrollPane, GroupLayout.PREFERRED_SIZE, 395, GroupLayout.PREFERRED_SIZE)
								.addGroup(jPanel1Layout.createSequentialGroup().addGap(20).addComponent(LabelDistrito)
										.addGap(11)
										.addComponent(ComboDistrito, GroupLayout.PREFERRED_SIZE, 41,
												GroupLayout.PREFERRED_SIZE)
										.addPreferredGap(ComponentPlacement.RELATED, 49, Short.MAX_VALUE)
										.addComponent(LabelBarrio).addGap(68)
										.addComponent(jButton1, GroupLayout.PREFERRED_SIZE, 41,
												GroupLayout.PREFERRED_SIZE)
										.addGap(105)))))
				.addContainerGap(39, Short.MAX_VALUE)));

		textArea = new JTextArea();
		textArea.setFont(new Font("Arial", Font.PLAIN, 18));
		scrollPane.setViewportView(textArea);
		jPanel1.setLayout(jPanel1Layout);

		javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
		layout.setHorizontalGroup(layout.createParallelGroup(Alignment.LEADING)
				.addGroup(layout.createSequentialGroup().addContainerGap()
						.addComponent(jPanel1, GroupLayout.PREFERRED_SIZE, 975, GroupLayout.PREFERRED_SIZE)
						.addContainerGap(813, Short.MAX_VALUE)));
		layout.setVerticalGroup(layout.createParallelGroup(Alignment.LEADING)
				.addGroup(layout.createSequentialGroup().addContainerGap()
						.addComponent(jPanel1, GroupLayout.PREFERRED_SIZE, 590, GroupLayout.PREFERRED_SIZE)
						.addContainerGap(GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)));
		getContentPane().setLayout(layout);

		pack();
	}// </editor-fold>

	private void buttonActionPerformed(java.awt.event.ActionEvent evt) {

		String resultado = new String("<html>");
		distrito = ComboDistrito.getItemAt(ComboDistrito.getSelectedIndex());
		barrio = ComboBarrio.getItemAt(ComboBarrio.getSelectedIndex());
		resultado = App.sparqlCalles(distrito, barrio);
		System.out.println(resultado);
		textArea.setText(resultado);
	}

	/**
	 * @param args the command line arguments
	 */
	public static void main(String args[]) {
		/* Set the Nimbus look and feel */
		// <editor-fold defaultstate="collapsed" desc=" Look and feel setting code
		// (optional) ">
		/*
		 * If Nimbus (introduced in Java SE 6) is not available, stay with the default
		 * look and feel. For details see
		 * http://download.oracle.com/javase/tutorial/uiswing/lookandfeel/plaf.html
		 */
		try {
			for (javax.swing.UIManager.LookAndFeelInfo info : javax.swing.UIManager.getInstalledLookAndFeels()) {
				if ("Nimbus".equals(info.getName())) {
					javax.swing.UIManager.setLookAndFeel(info.getClassName());
					break;
				}
			}
		} catch (ClassNotFoundException ex) {
			java.util.logging.Logger.getLogger(Interfaz.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
		} catch (InstantiationException ex) {
			java.util.logging.Logger.getLogger(Interfaz.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
		} catch (IllegalAccessException ex) {
			java.util.logging.Logger.getLogger(Interfaz.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
		} catch (javax.swing.UnsupportedLookAndFeelException ex) {
			java.util.logging.Logger.getLogger(Interfaz.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
		}
		// </editor-fold>

		/* Create and display the form */
		java.awt.EventQueue.invokeLater(new Runnable() {
			public void run() {
				new Interfaz().setVisible(true);
			}
		});
	}

	private javax.swing.JComboBox<String> ComboDistrito;
	private javax.swing.JComboBox<String> ComboBarrio;
	private javax.swing.JLabel LabelDistrito;
	private javax.swing.JLabel LabelBarrio;
	private javax.swing.JLabel LabelTitulo;
	private javax.swing.JPanel PanelColor;
	private javax.swing.JButton jButton1;
	private javax.swing.JPanel jPanel1;
	private JScrollPane scrollPane;
	private JTextArea textArea;
	private javax.swing.JButton btnDistritofrontera;
}