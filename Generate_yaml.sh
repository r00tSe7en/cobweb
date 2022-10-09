RESOLVER_IPS='active_subdomains/active_subdomains2ips.txt'
while read line; do
	domain=$(echo "$line" | awk '{print $1}')
	ip=$(echo "$line" | awk '{print $2}')
	if [[ -n "${ip}" ]]; then
		echo -e "${domain} = ${ip} " | tee -a "TMP_RESOLV.txt" &>/dev/null
	fi
done <${RESOLVER_IPS}

#Resolver IP = Subdomain {pars} Into YAML File
awk '{ if (a[$3]) a[$3] = a[$3]"\n - "$1; else a[$3]=":\n - "$1;} END { for (i in a) print i,a[i]}' <TMP_RESOLV.txt | sed -e 's/\s:/:/g' >active_subdomains/subdomains2ips.yaml
rm -r TMP_RESOLV.txt >/dev/null 2>&1
