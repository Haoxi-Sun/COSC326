import javax.swing.JFrame; 
import javax.swing.JTextField;
import javax.swing.JList;

import java.awt.Font;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.DefaultListModel;
import javax.swing.JButton;
import javax.swing.JLabel;
import javax.swing.JScrollPane;

public class GuiG extends JFrame{
    private JTextField textInput;
    
    private DefaultListModel<String> modelStack = new DefaultListModel<>();
    private DefaultListModel<String> modelQueue = new DefaultListModel<>();

    public GuiG(){
        setTitle("GUI for Stack and Queue");
        setSize(800, 600);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
        getContentPane().setLayout(null);

        //a new button for the tips to show in another frame
        JButton jbutton = new JButton("Open to tips");
        jbutton.setBounds(590,400,115,23);
        getContentPane().add(jbutton);

        JLabel labelJButton1 = new JLabel("If you don't know stack or queue");
        JLabel labelJButton2 = new JLabel("Please push here to get tips.");
        labelJButton1.setBounds(550,420,200,30);
        labelJButton2.setBounds(550,430,200,30);
        labelJButton1.setHorizontalAlignment(JLabel.CENTER);
        labelJButton2.setHorizontalAlignment(JLabel.CENTER);
        labelJButton1.setFont(new Font("",Font.CENTER_BASELINE,10));
        labelJButton2.setFont(new Font("",Font.CENTER_BASELINE,10));
        getContentPane().add(labelJButton1);
        getContentPane().add(labelJButton2);

        //when the user push the button "open to tips", there will be another frame shown
        jbutton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e){
                if(e.getSource()==jbutton){
                    new JFrame2();
                }
            }
        });

        JScrollPane scrollPaneStack = new JScrollPane();
        scrollPaneStack.setBounds(10,37,209,514);
        getContentPane().add(scrollPaneStack);

        JScrollPane scrollPaneQueue = new JScrollPane();
        scrollPaneQueue.setBounds(229,37,234,514);
        getContentPane().add(scrollPaneQueue);

        //the following code is for the text of input
        textInput = new JTextField();
        
        textInput.setBounds(547,55,209,21);
        getContentPane().add(textInput);
        textInput.setColumns(10);
        

        //add the label of "input"
        JLabel label3 = new JLabel("Input:");
        label3.setBounds(498,58,73,15);
        label3.setFont(new Font("",Font.BOLD,14));
        getContentPane().add(label3);
 
 
        //add label "stack"
        JLabel labelStack = new JLabel("Stack");
        labelStack.setBounds(90,10,73,15);
        labelStack.setFont(new Font("",Font.BOLD,18));
        getContentPane().add(labelStack);
 
        //add label "queue"
        JLabel labelQueue = new JLabel("Queue");
        labelQueue.setBounds(310,10,73,15);
        labelQueue.setFont(new Font("",Font.BOLD,18));
        getContentPane().add(labelQueue);

        JButton add = new JButton("Add");
        add.setBounds(590,150,115,23);
        getContentPane().add(add);

        JLabel labelAdd1 = new JLabel("Button add for adding value");
        JLabel labelAdd2 = new JLabel("to Stack and Queue.");
        labelAdd1.setBounds(500,170,300,23);
        labelAdd2.setBounds(500,180,300,23);
        labelAdd1.setHorizontalAlignment(JLabel.CENTER);
        labelAdd2.setHorizontalAlignment(JLabel.CENTER);
        labelAdd1.setFont(new Font("",Font.CENTER_BASELINE,10));
        labelAdd2.setFont(new Font("",Font.CENTER_BASELINE,10));
        getContentPane().add(labelAdd1);
        getContentPane().add(labelAdd2);

        JButton remove = new JButton("Remove");
        remove.setBounds(590,200,115,23);
        getContentPane().add(remove);

        JLabel labelRemove1 = new JLabel("Button add for removing value");
        JLabel labelRemove2 = new JLabel("from Stack and Queue.");
        labelRemove1.setBounds(500,220,300,23);
        labelRemove2.setBounds(500,230,300,23);
        labelRemove1.setHorizontalAlignment(JLabel.CENTER);
        labelRemove2.setHorizontalAlignment(JLabel.CENTER);
        labelRemove1.setFont(new Font("",Font.CENTER_BASELINE,10));
        labelRemove2.setFont(new Font("",Font.CENTER_BASELINE,10));
        getContentPane().add(labelRemove1);
        getContentPane().add(labelRemove2);

        //when the user push the button Add, the input value will add to the stack and queue
        add.addActionListener(new ActionListener(){
            @Override
            public void actionPerformed(ActionEvent e){
                if(e.getSource()==add){
                    JList<String> listStack = new JList<>(modelStack);
                    JList<String> listQueue = new JList<>(modelQueue);
                    scrollPaneStack.setViewportView(listStack);
                    scrollPaneQueue.setViewportView(listQueue);
                    if(!textInput.getText().isEmpty()){
                        modelStack.add(0,textInput.getText());
                        modelQueue.add(0,textInput.getText());
                        textInput.setText("");
                    }
                }
            }
        });

        //when the user push the buttom Remove, the value will remove from stack and queue
        remove.addActionListener(new ActionListener(){
            @Override
            public void actionPerformed(ActionEvent e){
                if(e.getSource()==remove){
                    JList<String> listStack = new JList<>(modelStack);
                    JList<String> listQueue = new JList<>(modelQueue);
                    scrollPaneStack.setViewportView(listStack);
                    scrollPaneQueue.setViewportView(listQueue);
                    if(modelStack.getSize() > 0 || modelQueue.getSize() > 0){
                        modelStack.remove(0);
                        modelQueue.removeElementAt(modelQueue.getSize() - 1);
                    }
                }
            }
        });
    }

    
    public static void main(String[] args){
        GuiG frame = new GuiG();
        frame.setVisible(true);
    }
}
class JFrame2 extends JFrame{
   
    public JFrame2(){
        setTitle("Tips");
        setSize(600,200);
        setVisible(true);
        //setDefaultCloseOperation(EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
        getContentPane().setLayout(null);

        JLabel stackTitle = new JLabel("Stack:");
        JLabel queueTitle = new JLabel("Queue:");
        stackTitle.setBounds(10,10,73,15);
        queueTitle.setBounds(10,80,73,15);
        getContentPane().add(stackTitle);
        getContentPane().add(queueTitle);
        
        JLabel tipsStack1 = new JLabel("Stack is a linear data structure which follows a particular order in which");
        JLabel tipsStack2 = new JLabel("the operations are performed.");
        JLabel tipsStack3 = new JLabel("The order may be FILO(First In Last Out).");
        tipsStack1.setBounds(90,10,500,15);
        tipsStack2.setBounds(90,25,500,15);
        tipsStack3.setBounds(90,40,500,15);
        JLabel tipsQueue1 = new JLabel("A Queue is a linear structure which follows a particular order in which");
        JLabel tipsQueue2 = new JLabel("the operations are performed.");
        JLabel tipsQueue3 = new JLabel("The order is First In First Out (FIFO).");
        tipsQueue1.setBounds(90,80,500,15);
        tipsQueue2.setBounds(90,95,500,15);
        tipsQueue3.setBounds(90,110,500,15);
        getContentPane().add(tipsStack1);
        getContentPane().add(tipsStack2);
        getContentPane().add(tipsStack3);
        getContentPane().add(tipsQueue1);
        getContentPane().add(tipsQueue2);
        getContentPane().add(tipsQueue3);
        
    }
}
