<!-- form for forgotten password -->
<html>
    <head>
        %include header
    </head>
    <h2>Forgot Password</h2><br>
    <p>Enter your username below and we'll send you an email to help you reset your password!</p>
    <form action="/forgot" method="post">
        Username<br/>
        <input type="text" name="username"/><br>
        <input type="submit" value="Send Request"/>
    </form>
</html>