<!-- page for new users to register -->
<html>
    <head>
        %include header
    </head>
    <h2>Sign Up</h2>
    <p>Fill out the forms below to register a new account!</p><br>
    <form action="/signup" method="post">
        Username:<br/>
        <input type="text" name="username"/><br/>
        Password:<br/>
        <input type="password" name="password"/><br/>
        Confirm Password:<br/>
        <input type="password" name="password_confirm"/><br/>
        Email:<br/>
        <input type="text" name="email"/><br/>
        <hr/>
        <input type="submit" value="Sign Up"/>
    </form>
</html>