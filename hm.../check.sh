#!/bin/bash
# ^^ αν δεν εισαι σε slackware βαλε env κτλ
# Αν υπάρχουν και άλλα paths που εσυ ξερεις προσθεσε τα.
# Σε γενικες γραμμες αυτο το script ειναι ενα καλούτσικο health-check...
BASE=https://my-site.gr

# 1. User enumeration (βγάζει usernames -> μισή δουλειά για brute force)
curl -s "$BASE/wp-json/wp/v2/users" | jq .
curl -sI "$BASE/?author=1"                      # 301 σε /author/<username>/ = leak
curl -s "$BASE/?rest_route=/wp/v2/users" | jq .

# 2. xmlrpc  DDoS amplification + brute force via system.multicall
curl -s "$BASE/xmlrpc.php" -d '<methodCall><methodName>system.listMethods</methodName></methodCall>'
#   Αν απαντάει με methods -> κλείσ' το (ή περιόρισέ το)

# 3. Version / info leaks
curl -sI "$BASE/readme.html"                    # 200 = έκδοση WP εκτεθειμένη
curl -s  "$BASE/feed/" | grep -i generator      # generator στο RSS
curl -sI "$BASE/wp-links-opml.php"

# 4. Directory listing / αφημένα αρχεία
curl -s  "$BASE/wp-content/uploads/"            # ψάξε "Index of"
curl -sI "$BASE/wp-content/debug.log"           # 200 = leak (paths, errors)
curl -sI "$BASE/.git/HEAD"                      # εκτεθειμένο repo
curl -sI "$BASE/wp-config.php.bak"              # + .save .old ~ .txt .swp
curl -sI "$BASE/wp-content/uploads/backups/"

# 5. Admin / login επιφάνεια
curl -sI "$BASE/wp-admin/"                      # redirect σε login = ok
curl -sI "$BASE/wp-login.php"                   # υπάρχει rate-limit / 2FA;

# 6. REST API  τι εκθέτει συνολικά
curl -s  "$BASE/wp-json/" | jq '.routes | keys'
