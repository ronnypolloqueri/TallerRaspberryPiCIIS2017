<!--
    DEVICE MAP TO PIN(GPIO)
    DEVICE 1 pin7   (GPIO4)      
    DEVICE 2 pin7   (GPIO17)      
    DEVICE 3 pin7   (GPIOl8)      
    DEVICE 4 pin7   (GPIO21)      
    DEVICE 5 pin7   (GPIO22)      
    DEVICE 6 pin7   (GPIO23)      
-->
<?php


$script = 'python /home/pi/GPIO/automate.py ';

if (isset($_POST['1ON']))
{
exec($script . '7 0');
}
if (isset($_POST['1OFF']))
{
exec($script . '7 1');
}
if (isset($_POST['2ON']))
{
exec($script . '11 0');
}
if (isset($_POST['2OFF']))
{
exec($script . '11 1');
}
?>
<html> 
    <head>
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css" integrity="sha384-PsH8R72JQ3SOdhVi3uxftmaW6Vc51MKb0q5P2rRUpPvrszuE4W1povHYgTpBfshb" crossorigin="anonymous">

    </head>
    <body> 
        <form method="post"> 
            <table style="width: 20%; text-align: left; margin-left: auto; margin-right: auto;" border="0" cellpadding="4" cellspacing="0"> 
                <tr> 
                    <td style="text-align: center;">DEVICE 1</td> <td style="text-align: center;"><button class="btn btn-info" name="1ON"><span class="glyphicon glyphicon-plus"></span>ON</button>
                    </td> 
                    <td style="text-align: center;"><button class="btn btn-danger" name="1OFF">OFF</button></td> </tr> <tr> <td style="text-align: center;">DEVICE 2</td> <td style="text-align: center;"><button class="btn btn-info" name="2ON">ON</button>
                    </td> 
                    <td style="text-align: center;"><button class="btn btn-danger" name="2OFF">OFF</button>
                    </td> 
                </tr>
            </table> 
        </form> 
    </body> 
</html>
