PROJECTE FINAL DE PROGRAMACIÓ PER A LA CIÈNCIA DE DADES

- El projecte està fet per tal que amb executar el main sigui suficient
per a veure tot el procès. Val a dir que quan es crea una gràfica,
cal tancar-la per tal de que segueixi l'execució

------------------ INDEX ------------
Linia 14 - Respostes teòriques (Ex1.2 / Ex1.3)
Linia 28 - Packages
Linia 40 - Main
Linia 44 - Altres llibreries
Linia 48 - Ús de Git
Linia 59 - Altra informació - Setup.py

------- Respostes teòriques ---------
Respecte l'excercici 1.2, penso que no caldria tocar res ja que 1Gb no
em sembla que sigui un fitxer molt molt gran. És per això que crec
haver donat la resposta més òptima per a fitxers relativament petits.

Quan per contra parlem de l'excercici 1.3 (fitxer de 100Gb), està clar
que es podria quedar petit. La manera més sencilla que em ve al cap
per a resoldre-ho, seria implementar tasques asincrones o multitasking.
En aquest sentit també penso que es podria treballar amb alguna eina
de CI/CD (Continuous Integration / Continuous Deployment), com ara Jenkins
que faciliten aquestes tasques. Simplement hauriem d'executar el fitxer
segons uns paràmetres que podrien ser per exemple, que cada executor
llegeixi el 10% del fitxer.

--------- Packages ----------
Cada package està dedicat per a cada excercici concret. Els noms
són Excercici1Package, Excercici2Package, Excercici3Package,
Excercici4Package.
Tots ells son importats al fitxer main.py per tal de executar les seves
funcions

Excercici1Package -> import re, 3 funcions
Excercici2Package -> import pandas, 3 funcions
Excercici3Package -> import matplotlib, numpy, 3 funcions
Excercici4Package -> import matplotlib, 5 funcions

----- Main ------
El fitxer main només importa els packages mencionats a dalt.
Imprimeix informació per pantalla i crida a les funcions

----- Altres llibreries -----
Podeu trobar totes les llibreries al fitxer requirements.txt, generat
mitjançant la comanda pip freeze > requirements.txt

-------- Ús de Git --------
el Classroom proporcionat estava caducat quan vaig provar de treballar
des d'allà. Vaig decidir no treballar amb Git desprès d'aquest fet
ja que realment a la meva feina acostumo a treballar amb git i sé com
fer-ho. D'entrada es crea un repositori on farem els commits.
Amb git status comprovem quins fitxers no tenim a github,
seguidament fem git add nomfitxer per a preparar-lo pel commit
en següent lloc commit -m 'Missatge del commit'
finalment fem un push per a aplicar els canvis.

-------------- Altra informació --------------
Quan he intentat pujar el setup.py mitjançant
pip install yourpackage
python setup.py register
python setup.py upload

M'ha donat el següent error que no he estat capaç de resoldre:

Upload failed (403): Invalid or non-existent authentication information. See https://pypi.org/help/#invalid-auth for more information.
error: Upload failed (403): Invalid or non-existent authentication information. See https://pypi.org/help/#invalid-auth for more information.

He seguit fent proves pero em segueix donant errors:
Invalid or non-existent authentication information. See https://test.pypi.org/help/#invalid-auth for more information.
Just desprès d'afegir com a username i password la conta que acabo de crear al propi site
De la mateixa manera he probat a crear un API Token desde la web (user: __token__ , password: pypi-AgEIcHlwaS5vcmcCJDA1YzFiMGUxLWU4MmEtNGUzMS04OGMwLTMyY2RhMTZjNDRjZAACJXsicGVybWlzc2lvbnMiOiAidXNlciIsICJ2ZXJzaW9uIjogMX0AAAYgm73P6lTTWF5eLzhCEg5jis6lyK61doJo-QQVK6I2MZo
i tampoc funciona.

Potser per això el fitxer setup.py finalment no té cap funcionalitat
Si funciones seria mitjançant la comanda:
python -m pip install --index-url https://test.pypi.org/simple/ --no-deps testpypi-jtorrenth

On python es un alias, depen de la maquina podria ser py...
