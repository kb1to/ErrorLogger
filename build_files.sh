echo "BUILD START"
uv pip install --system --break-system-packages -r requirements.txt
python3.12 manage.py collectstatic --noinput --clear
echo "BUILD END"