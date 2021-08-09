<!-- homepage -->
<!DOCTYPE html>
<html>
    <head>
        %include header
        <title>Atlas</title>
    </head>
    <body>
        %include banner
        %if message:
            %include('alert.tpl', message=message)
        %end
        %include navigation
        <br>
        <div class="subtitle">
            <b><u>Your Atlas</u></b>
        </div><br><br>
            %include atlas_list
        <div class="homeimg">
            %include drawing
        </div>
        <div class="about">
            <p><b>Atlas</b> is a site for all to catalogue their favorite places from the past, present, and future.</p>
            <p>With a free user account, anyone is able to enter whatever place they choose and any extra details associated with it, such as when they visited it or when they plan to, and any specific comments they may have about it.</p>
            <p>Users also have access to an in-site map of the Earth that can be used to easily find all of their places. Whether they're on there or not, we hope it will serve you well in your cataloguing journey.</p>
            <p>Interested? Sign up today and map out your world with Atlas!</p>
        </div><br>
        <p><span class="material-icons md-24">schedule</span> This page was last updated on August 8, 2021.</p>
    </body>
</html>