
/**
 * Etude 5 Look Who's Talking
 * @author Ella Ji 2854080 & Elsie Sun 4468203 
 */

import java.util.*;

public class LookWhoTalking{
    public static void main(String[] args){
        LookWhoTalking lookwho = new LookWhoTalking();
        Scanner sc = new Scanner(System.in);
        while(sc.hasNextLine()){
            String line = sc.nextLine().toLowerCase();
            String result = lookwho.translate(line);

            // quit the program
            if(line.length()==0){
                break;
            }
            // print the result
            System.out.println(result);
        }
    }

    /** 
     * three lists for storing three tenses of verbs
     * the last list for storing meanings of verbs in Maori
     */
    String[] verbs_present = new String[] {"go","make","see","want","call","ask","read","learn"};
    String[] verbs_past = new String[] {"went","made","saw","wanted","called","asked","read","learned"};
    String[] verbs_ing = new String[] {"going","making","seeing","wanting","calling","asking","reading","learning"};
    String[] verbs_meanings = new String[] {"haere","hanga","kite","hiahia","karanga","pātai","pānui","ako"};

    String verbType;

    /**
     * a method to find the verb in lists of verbs in different tenses
     * and defind a type of the verb
     * @param verb verb
     * @return return index of list if verb in any three lists, otherwise return -1
     */
    public int findVerb(String verb){

        for(int i=0;i<verbs_present.length;i++){
            // the present tense of verbs
            if(verbs_present[i].equals(verb)){
                verbType = "present";
                return i;
            }
            // the present progressive tense of verbs
            if(verbs_ing[i].equals(verb)){
                verbType = "present";
                return i;
            }
            // the past tense of verbs
            if(verbs_past[i].equals(verb)){
                verbType = "past";
                return i;
            }
        }
        return -1;
    }

    /**
     * translate English to Mario
     * @param line the sentence is users entered
     * @return the result or error messages
     */
    public String translate(String line){
        // make the characters in the string to lowercase
        line = line.toLowerCase();

        // determine whether or not there are brackets
        int indexOfLeftBracket = -1;
        int indexOfRightBracket = -1;

        // count them if there are brackets
        for(int i=0;i<line.length();i++){
            char ch = line.charAt(i);
            if(ch == '('){
                indexOfLeftBracket = i;
            }
            if(ch == ')'){
                indexOfRightBracket = i;
            }
        }

        String hint = null;
        // if there are brackets
        // store the hint between two brackets and the sentence users input without brackets
        if(indexOfLeftBracket != -1 && indexOfRightBracket != -1){
            hint = line.substring(indexOfLeftBracket + 1, indexOfRightBracket);
            line = line.substring(0,indexOfLeftBracket) + line.substring(indexOfRightBracket + 1, line.length());
        }

        boolean hasHint = hint != null;
        int hintNumber = 0;

        // determine types of hint
        // the default type is 'excl'
        String hintType = "excl";
        if(hasHint){
            String[] items = hint.split("\\s+");

            // the sentence is invalid in below conditions
            if(items.length != 2){
                return "invalid sentence";
            }
            if(!isNumber(items[0])){
                return "invalid sentence";
            }

            hintNumber = Integer.parseInt(items[0]);
            hintType = items[1];

            if(!hintType.equals("excl") && !hintType.equals("incl")){
                return "invalid sentence";
            }
        }
        // split the sentence
        // store each character into list
        String[] words = line.split("\\s+");
        if(words.length == 2 || words.length == 3){
            
            // the sentence structures
            String subject = words[0];
            String verb = words[words.length - 1];
            String middle = "";
            if(words.length==3){
                middle = words[1];
            }

            int indexOfVerb = findVerb(verb);
            
            // if the verb is not found
            if(indexOfVerb == -1){
                return "unknown verb \"" + verb + "\"";
            }

            String part1 = "";
            // translate English to Mario
            String part2 = verbs_meanings[indexOfVerb];
            
            // if the type of the verb is present tense
            if(verbType.equals("present")){
                part1 = "Kei te";
                
                // the sentence is future tense if there is 'will'
                if(middle.equals("will")){
                    part1 = "Ka";
                }
            
            // it the type of the verb is past tense
            }else if(verbType.equals("past")){
                part1 = "I";
            }else{
                part1 = "Kei te";
            }

            String part3 = "";
            // if the subject is 'we'
            if(subject.equals("we")){

                if(hasHint){
                    // hintType is include both speaker and listener
                    if(hintType.equals("incl")){
                        // two people
                        if(hintNumber==2){
                            part3 = "tāua";
                        }else{
                            part3 = "tātou";
                        }
                    }else{
                        // if excludes the listeners, two people
                        if(hintNumber==2){
                            part3 = "māua";
                        }else{
                            part3 = "mātou";
                        }
                    }
                }else{
                    part3 = "māua";
                }
            // if the subject is 'i'
            }else if(subject.equals("i")){
                part3 = "au";
            // if the subject is 'he' or 'she'
            }else if(subject.equals("he") || subject.equals("she")){
                part3 = "ia";
            // if the subject is 'you'
            }else if(subject.equals("you")){
                if(hasHint){
                    if(hintNumber==2){
                        //two people
                        part3 = "kōrua";
                    }else if(hintNumber>=3){
                        //three people
                        part3 = "koutou";
                    }else{
                        part3 = "koe";
                    }
                }else{
                    part3 = "koe";
                }
            // if the subject is 'they'
            }else if(subject.equals("they")){
                if(hasHint){
                    if(hintNumber==2){
                        part3 = "rāua";
                    }else{
                        part3 = "rātou";
                    }
                }else{
                    part3 = "rāua";
                }
            }
            return part1 + " " + part2 + " " + part3;
        }else{
            return "invalid sentence";
        }
    }

    /**
     * to check the item in the string is number or not
     * @param str the string users input
     * @return return true if the string is number, otherwise return false
     */
    private static boolean isNumber(String str){
        for(int i=0;i<str.length();i++){
            if(!isNumber(str.charAt(i))){
                return false;
            }
        }
        return true;
    }

    /**
     * determine if characters are number
     * @param ch is a character
     * @return True if the character is bigger than or equals 0 and less than or equals 9
     */
    private static boolean isNumber(char ch){
        return ch >= '0' && ch <= '9';
    }
}