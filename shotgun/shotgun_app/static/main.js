/*****************************************************************************
 * main.js                                                                   *
 *                                                                           *  
 * Provides main functions and helper functions for website that dynamically *
 * changes the html of the page given user input:                            *
 *                                                                           *
 * Max Lu and Linda Du                                                       *
 *****************************************************************************/
 
 
/**
 * Loads contact list by changing option div's html by calling the addFriendToList
 * method for each contact in contacts global variable. Also creates a button that
 * loads a form to add a contact.
 */
 
function loadCreateForm() {
    var form = "<br/><p><input name=\"ename\" type=\"text\" placeholder=\"Event Name\" /></p>";
    form += "<p><textarea rows=\"5\" cols=\"50\" name=\"edescription\" placeholder=\"Event Description\" /></textarea></p>";
    form += "<p>Privacy<br/><input type=\"radio\" name=\"privacy\" id=\"0\" value=\"friends\" />&nbsp;&nbsp;friends&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;";
    form += "<input type=\"radio\" name=\"privacy\" id=\"1\" value=\"friends of friends\" />&nbsp;&nbsp;friends of friends&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;";
    form += "<input type=\"radio\" name=\"privacy\" id=\"2\" value=\"errone\" />&nbsp;&nbsp;errone<br/>";
    form += "</p><br/>Optional: <br/><p><input name=\"location\" type=\"text\" placeholder=\"Location\" /></p>";
    form += "Event date: <input type=\"date\" name=\"edate\"> <input type=\"time\" name=\"etime\"><br/>"; 
    form += "<input type=\"submit\" value=\"Create\" /></form>";
    $('#create').html(form);
}

/*
 * Executed when page loads
 */
$(document).ready(function () {   
   
});