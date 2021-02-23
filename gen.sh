cat base.yml > mkdocs.yml
echo "# Welcome to My Collection\n\n" > docs/index.md

echo "  - Home: index.md" >> mkdocs.yml
for file in `ls docs/*.md`
do
	filename="${file##*/}"
	nameonly="${filename%.*}"
	if [ "${nameonly}" != "index" ]; then
		echo "  - ${nameonly}: ${filename}" >> mkdocs.yml
		header=$(head -1 docs/${filename} | cut -d '#' -f2)
		echo "[${header}](${filename})  " >> docs/index.md
	fi
done
