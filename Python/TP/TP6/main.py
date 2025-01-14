import subprocess
import argparse
import os

def traceroute(target, progressive, output_file):
    # Prépare la commande traceroute
    command = ["traceroute", target]

    # Ouvre le fichier de sortie si spécifié
    output = None
    if output_file:
        output = open(output_file, "w")

    try:
        # Si mode progressif
        if progressive:
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            for line in process.stdout:
                ip_address = extract_ip_from_line(line)
                if ip_address:
                    print(ip_address)
                    if output:
                        output.write(ip_address + "\n")
            process.wait()
        else:
            # Mode par défaut (liste complète à la fin)
            result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if result.returncode == 0:
                ips = [extract_ip_from_line(line) for line in result.stdout.splitlines() if extract_ip_from_line(line)]
                for ip in ips:
                    print(ip)
                if output:
                    output.write("\n".join(ips) + "\n")
            else:
                print("Erreur lors de l'exécution de traceroute :", result.stderr)

    except subprocess.SubprocessError as e:
        print("Erreur lors de l'exécution de traceroute :", e)

    finally:
        if output:
            output.close()

def extract_ip_from_line(line):
    import re
    # Extraire l'adresse IP avec une regex
    match = re.search(r'\((\d+\.\d+\.\d+\.\d+)\)', line)
    return match.group(1) if match else None

def main():
    parser = argparse.ArgumentParser(description="Script traceroute avec options avancées.")
    parser.add_argument("target", help="URL ou adresse IP cible pour le traceroute.")
    parser.add_argument("-p", "--progressive", action="store_true", help="Afficher les résultats au fur et à mesure.")
    parser.add_argument("-o", "--output-file", help="Nom du fichier pour enregistrer les résultats du traceroute.")

    args = parser.parse_args()

    traceroute(args.target, args.progressive, args.output_file)

if __name__ == "__main__":
    main()