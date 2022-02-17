/*
3

1) generate all possible outcomes
2) if an outcome is valid add it to the results

1)generate only the valid outcomes



lets think about what a valid outcome is
1) always start with an opening paren
2) number of closed should never be greater than the number of open parens
3) at the end, the number of open and closed parens should be equal

*/

class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> allValidParens = new ArrayList<String>();
        String curParen = "";
        
        generateAllParens(n, n, allValidParens, curParen);
        
        return allValidParens;
    }
    
    public void generateAllParens(int remOpen, int remClosed, List<String> allValidParens, String curParen) {

        if(remOpen == 0 && remClosed == 0) {
            allValidParens.add(curParen);
            return;
        }
        
        if(remOpen > remClosed) return;
        
        // add an open paren if possible
        if(remOpen > 0) {
            generateAllParens(remOpen - 1, remClosed, allValidParens, curParen + "(");
        }
        
        // adding a closed paren if possible
        if(remClosed > 0 && remClosed > remOpen) {
            generateAllParens(remOpen, remClosed - 1, allValidParens, curParen + ")");
        }
        
        return;
    }
    
}