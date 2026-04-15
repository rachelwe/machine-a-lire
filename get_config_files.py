import yaml

def get_config(collection=""):
   if collection:
      config_path = "/home/pi/Documents/machine-a-lire/images/" + collection + "/config.yml"
   else:
      config_path = "/home/pi/Documents/machine-a-lire/images/config.yml"
   try:
      with open(config_path) as f:
         config = yaml.safe_load(f)
      return config
   except yaml.YAMLError as e:
      return jsonify({"error": f"Error parsing YAML: {e}"}), 400
   except FileNotFoundError:
      return {}