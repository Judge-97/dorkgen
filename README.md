# DorkGen

<div align="center">
  <img src="src/logo.png" alt="LinkHound Logo" width="150" height="200"/>
  <p>dorkgen: A lightweight frontend tool for generating powerful Google/Bing dorks for reconnaissance and OSINT.</p>
</div>


---

DorkGen is a lightweight, frontend-only **dork generator** for security recon and Google/Bing-based searching. It helps you quickly compose dynamic dorks (site:, intitle:, inurl:, intext:, filetype:, OR logic, etc.), experiment with parameter patterns, and save your history locally in the browser.

---

## Features

* Build complex Google/Bing dorks with common operators: `site:`, `intitle:`, `inurl:`, `intext:`, `filetype:`.
* Combine clauses using `OR` or boolean grouping.
* Quick parameter injection for testing common query patterns.
* History saved to `localStorage` — keeps your recent dorks across sessions.


## Demo / Quick start

1. Clone the repo:

```bash
git clone https://github.com/NakuTenshi/dorkgen.git
cd dorkgen
```

> Note: you can install the application by running `./install.sh` for haveing a flask application or you can open the `index.html` by your browser

2. Install the Application (flask application)

```bash
pip3 install -r requrments.txt
sudo chmod 777 install.sh
sudo ./install.sh
```

3. Run the application

```bash
dorkgen
```
> it runs the application at `127.0.0.1:1234`

---

created by: **NakuTenshi**




