# Django REST Framework with Unit TEST

<h2>Installation</h2>
<b>create a folder in login directory</b>
<pre>
mkdir djangorest
cd djangorest
</pre>
<b>create a virtualenv named env</b>
<pre>
python3 -m venv env
</pre>
<b>Verify that virtualenv is working. (at the beginning of the command request (env))</b>
<pre>
(env) ~$ pip install --upgrade pip
</pre>
<b>then install django</b>
<pre>
(env) ~$ pip3 install django
</pre>
<b><install the rest framework</b>
<pre>(env) ~$ pip3 install djangorestframework</pre>
<h2>Usage</h2>
<b>Create the Database</b>

<pre>
python manage.py makemigrations
python manage.py migrate
</pre>

<h2>Unit Tests</h2>
<b>Run tests</b>
<pre>
python manage.py test
</pre>
