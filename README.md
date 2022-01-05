# Easy Django Deployment CLI (Under Development)

##### Deploy Django + Gunicorn + NGINX with Single Command

Deploying Django takes to much efforts, so i made this program, this program will deploy Django on any VPS with Gunicorn + NGINX enabled and all wraped in Python Environment.

Only supported in Linux OS

Features
[x] Deploy Entire Project with Single Command
[x] Push Updates with minimal Downtime

### **Get $100 Free Credits on [Vultr](https://www.vultr.com/?ref=7168946) (Affiliate Link)**

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/tonraj)

# How to Use?

```
python easyd.py --help  # to view all available options and arguments
```

*Example Commands*
**Deploy GIT Project**
```
python easyd.py GIT --git-url http://da:dasd@gmail.com --python_version 3.8 --requirments req.txt --collect-static --migrate --project_name test --domain www.test.com test.com
```

**Setup New**
```
python easyd.py NEW --python_version 3.8 --django_version 4.2 --migrate --project_name test  --domain www.test.com test.com
```
