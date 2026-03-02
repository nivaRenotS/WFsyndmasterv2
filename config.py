# config.py
# Taken from https://wiki.warframe.com/w/Warframe_Augment_Mods/PvE?action=edit
RAW_WIKI_DATA = """
{| class="wikitable" style="width:100%;" align="center"
|-
! Warframes
! Augment Mods
! Favored Syndicates
|-
| {{WF|Ash}}
| {{M|Seeking Shuriken}} {{M|Smoke Shadow}} {{M|Teleport Rush}} {{M|Rising Storm}}
| {{Faction|Arbiters of Hexis}}<br />{{Faction|Red Veil}}
|-
| {{WF|Atlas}}
| {{M|Rubble Heap}} {{M|Path of Statues}} {{M|Tectonic Fracture}} {{M|Ore Gaze}} {{M|Titanic Rumbler}}
| {{Faction|Steel Meridian}}<br />{{Faction|Red Veil}}
|-
| {{WF|Banshee}}
| {{M|Sonic Fracture}} {{M|Resonance}} {{M|Savage Silence}} {{M|Resonating Quake}}
| {{Faction|Cephalon Suda}}<br />{{Faction|The Perrin Sequence}}
|-
| {{WF|Baruuk}}
| {{M|Elusive Retribution}} {{M|Endless Lullaby}} {{M|Reactive Storm}}
| {{Faction|Arbiters of Hexis}}<br />{{Faction|New Loka}}
|-
| {{WF|Caliban}}
| {{M|Razor Mortar}}
| {{Faction|Cephalon Suda}}<br />{{Faction|The Perrin Sequence}}
|-
| {{WF|Chroma}}
| {{M|Everlasting Ward}} {{M|Guardian Armor}} {{M|Vexing Retaliation}} {{M|Guided Effigy}}
| {{Faction|Cephalon Suda}}<br />{{Faction|The Perrin Sequence}}
|-
| {{WF|Citrine}}
| {{M|Prismatic Companion}} {{M|Recrystalize}}
| {{Faction|Steel Meridian}}<br />{{Faction|Red Veil}}
|-
| {{WF|Dagath}}
| {{M|Spectral Spirit}}
| {{Faction|Red Veil}}<br />{{Faction|The Perrin Sequence}}
|-
| {{WF|Ember}}
| {{M|Fireball Frenzy}} {{M|Immolated Radiance}} {{M|Healing Flame}} {{M|Exothermic}}
| {{Faction|Steel Meridian}}<br />{{Faction|Red Veil}}
|-
| {{WF|Equinox}}
| {{M|Duality}} {{M|Calm & Frenzy}} {{M|Peaceful Provocation}} {{M|Energy Transfer}}
| {{Faction|Arbiters of Hexis}}<br />{{Faction|New Loka}}
|-
| {{WF|Excalibur}}
| {{M|Surging Dash}} {{M|Radiant Finish}} {{M|Furious Javelin}} {{M|Chromatic Blade}}
| {{Faction|Arbiters of Hexis}}<br />{{Faction|Steel Meridian}}
|-
| {{WF|Excalibur Umbra}}
| {{M|Warrior's Rest}}
| {{Faction|Arbiters of Hexis}}<br />{{Faction|Red Veil}}
|-
| {{WF|Frost}}
| {{M|Biting Frost}} {{M|Freeze Force}} {{M|Ice Wave Impedance}} {{M|Chilling Globe}} {{M|Icy Avalanche}}
| {{Faction|Cephalon Suda}}<br />{{Faction|Steel Meridian}}
|-
| {{WF|Gara}}
| {{M|Shattered Storm}} {{M|Mending Splinters}} {{M|Spectrosiphon}}
| {{Faction|Arbiters of Hexis}}<br />{{Faction|New Loka}}
|-
| {{WF|Garuda}}
| {{M|Dread Ward}} {{M|Blood Forge}} {{M|Blending Talons}}
| {{Faction|Steel Meridian}}<br />{{Faction|Red Veil}}
|-
| {{WF|Gauss}}
| {{M|Mach Crash}} {{M|Thermal Transfer}}
| {{Faction|Arbiters of Hexis}}<br />{{Faction|The Perrin Sequence}}
|-
| {{WF|Grendel}}
| {{M|Gourmand}} {{M|Hearty Nourishment}} {{M|Catapult}} {{M|Gastro}}
| {{Faction|Steel Meridian}}<br />{{Faction|Red Veil}}
|-
| {{WF|Gyre}}
| {{M|Coil Recharge}} {{M|Cathode Current}} {{M|Conductive Sphere}} {{M|Reverse Rotorswell}}
| {{Faction|Arbiters of Hexis}}<br />{{Faction|The Perrin Sequence}}
|-
| {{WF|Harrow}}
| {{M|Tribunal}} {{M|Warding Thurible}} {{M|Lasting Covenant}}
| {{Faction|Arbiters of Hexis}}<br />{{Faction|Red Veil}}
|-
| {{WF|Hildryn}}
| {{M|Balefire Surge}} {{M|Blazing Pillage}} {{M|Aegis Gale}}
| {{Faction|Cephalon Suda}}<br />{{Faction|The Perrin Sequence}}
|-
| {{WF|Hydroid}}
| {{M|Viral Tempest}} {{M|Tidal Impunity}} {{M|Rousing Plunder}} {{M|Pilfering Swarm}}
| {{Faction|Cephalon Suda}}<br />{{Faction|New Loka}}
|-
| {{WF|Inaros}}
| {{M|Elemental Sandstorm}} {{M|Negation Armor}} {{M|Desiccation's Curse}}
| {{Faction|Arbiters of Hexis}}<br />{{Faction|The Perrin Sequence}}
|-
| {{WF|Ivara}}
| {{M|Empowered Quiver}} {{M|Piercing Navigator}} {{M|Infiltrate}} {{M|Concentrated Arrow}}
| {{Faction|Cephalon Suda}}<br />{{Faction|The Perrin Sequence}}
|-
| {{WF|Jade}}
| {{M|Jade's Judgment}}
| {{Faction|Arbiters of Hexis}}<br />{{Faction|Red Veil}}
|-
| {{WF|Khora}}
| {{M|Accumulating Whipclaw}} {{M|Venari Bodyguard}} {{M|Pilfering Strangledome}}
| {{Faction|Steel Meridian}}<br />{{Faction|Red Veil}}
|-
| {{WF|Koumei}}
| {{M|Omikuji's Fortune}}
| {{Faction|Arbiters of Hexis}}<br />{{Faction|New Loka}}
|-
| {{WF|Kullervo}}
| {{M|Volatile Recompense}} {{M|Wrath of Ukko}}
| {{Faction|Steel Meridian}}<br />{{Faction|New Loka}}
|-
| {{WF|Lavos}}
| {{M|Valence Formation}} {{M|Swift Bite}} {{M|Lingering Transmutation}}
| {{Faction|New Loka}}<br />{{Faction|Red Veil}}
|-
| {{WF|Limbo}}
| {{M|Rift Haven}} {{M|Rift Torrent}} {{M|Cataclysmic Continuum}}
| {{Faction|Arbiters of Hexis}}<br />{{Faction|Cephalon Suda}}
|-
| {{WF|Loki}}
| {{M|Savior Decoy}} {{M|Hushed Invisibility}} {{M|Safeguard Switch}} {{M|Irradiating Disarm}} {{M|Damage Decoy}}
| {{Faction|Arbiters of Hexis}}<br />{{Faction|Red Veil}}
|-
| {{WF|Mag}}
| {{M|Greedy Pull}} {{M|Magnetized Discharge}} {{M|Counter Pulse}} {{M|Fracturing Crush}}
| {{Faction|New Loka}}<br />{{Faction|The Perrin Sequence}}
|-
| {{WF|Mesa}}
| {{M|Ballistic Bullseye}} {{M|Muzzle Flash}} {{M|Staggering Shield}} {{M|Mesa's Waltz}}
| {{Faction|Steel Meridian}}<br />{{Faction|Red Veil}}
|-
| {{WF|Mirage}}
| {{M|Hall of Malevolence}} {{M|Explosive Legerdemain}} {{M|Total Eclipse}}
| {{Faction|Arbiters of Hexis}}<br />{{Faction|Cephalon Suda}}
|-
| {{WF|Nekros}}
| {{M|Soul Survivor}} {{M|Creeping Terrify}} {{M|Despoil}} {{M|Shield of Shadows}}
| {{Faction|Red Veil}}<br />{{Faction|The Perrin Sequence}}
|-
| {{WF|Nezha}}
| {{M|Pyroclastic Flow}} {{M|Reaping Chakram}} {{M|Safeguard}} {{M|Controlled Slide}} {{M|Divine Retribution}}
| {{Faction|Cephalon Suda}}<br />{{Faction|Steel Meridian}}
|-
| {{WF|Nidus}}
| {{M|Abundant Mutation}} {{M|Teeming Virulence}} {{M|Larva Burst}} {{M|Parasitic Vitality}} {{M|Insatiable}}
| {{Faction|Steel Meridian}}<br />{{Faction|The Perrin Sequence}}
|-
| {{WF|Nova}}
| {{M|Neutron Star}} {{M|Antimatter Absorb}} {{M|Escape Velocity}} {{M|Molecular Fission}}
| {{Faction|Cephalon Suda}}<br />{{Faction|Steel Meridian}}
|-
| {{WF|Nyx}}
| {{M|Mind Freak}} {{M|Pacifying Bolts}} {{M|Chaos Sphere}} {{M|Assimilate}}
| {{Faction|Arbiters of Hexis}}<br />{{Faction|New Loka}}
|-
| {{WF|Oberon}}
| {{M|Smite Infusion}} {{M|Hallowed Eruption}} {{M|Phoenix Renewal}} {{M|Hallowed Reckoning}}
| {{Faction|Steel Meridian}}<br />{{Faction|New Loka}}
|-
| {{WF|Octavia}}
| {{M|Partitioned Mallet}} {{M|Conductor}}
| {{Faction|Cephalon Suda}}<br />{{Faction|New Loka}}
|-
| {{WF|Protea}}
| {{M|Repair Dispensary}} {{M|Temporal Erosion}} {{M|Temporal Artillery}}
| {{Faction|Arbiters of Hexis}}<br />{{Faction|The Perrin Sequence}}
|-
| {{WF|Qorvex}}
| {{M|Wrecking Wall}} {{M|Fused Crucible}}
| {{Faction|Cephalon Suda}}<br />{{Faction|Steel Meridian}}
|-
| {{WF|Revenant}}
| {{M|Thrall Pact}} {{M|Mesmer Shield}} {{M|Blinding Reave}}
| {{Faction|Cephalon Suda}}<br />{{Faction|The Perrin Sequence}}
|-
| {{WF|Rhino}}
| {{M|Ironclad Charge}} {{M|Iron Shrapnel}} {{M|Piercing Roar}} {{M|Reinforcing Stomp}}
| {{Faction|Steel Meridian}}<br />{{Faction|The Perrin Sequence}}
|-
| {{WF|Saryn}}
| {{M|Revealing Spores}} {{M|Venom Dose}} {{M|Regenerative Molt}} {{M|Contagion Cloud}}
| {{Faction|Steel Meridian}}<br />{{Faction|Red Veil}}
|-
| {{WF|Sevagoth}}
| {{M|Shadow Haze}} {{M|Dark Propagation}}
| {{Faction|Cephalon Suda}}<br />{{Faction|The Perrin Sequence}}
|-
| {{WF|Styanax}}
| {{M|Axios Javelineers}} {{M|Tharros Lethality}} {{M|Intrepid Stand}}
| {{Faction|Arbiters of Hexis}}<br />{{Faction|New Loka}}
|-
| {{WF|Titania}}
| {{M|Spellbound Harvest}} {{M|Beguiling Lantern}} {{M|Razorwing Blitz}} {{M|Ironclad Flight}}
| {{Faction|Red Veil}}<br />{{Faction|New Loka}}
|-
| {{WF|Trinity}}
| {{M|Pool of Life}} {{M|Vampire Leech}} {{M|Abating Link}} {{M|Champion's Blessing}}
| {{Faction|New Loka}}<br />{{Faction|The Perrin Sequence}}
|-
| {{WF|Valkyr}}
| {{M|Swing Line}} {{M|Eternal War}} {{M|Prolonged Paralysis}} {{M|Enraged}} {{M|Hysterical Assault}}
| {{Faction|New Loka}}<br />{{Faction|The Perrin Sequence}}
|-
| {{WF|Vauban}}
| {{M|Tesla Bank}} {{M|Photon Repeater}} {{M|Repelling Bastille}}
| {{Faction|Cephalon Suda}}<br />{{Faction|The Perrin Sequence}}
|-
| {{WF|Volt}}
| {{M|Shock Trooper}} {{M|Shocking Speed}} {{M|Transistor Shield}} {{M|Capacitance}}
| {{Faction|Arbiters of Hexis}}<br />{{Faction|Red Veil}}
|-
| {{WF|Voruna}}
| {{M|Prey of Dynar}} {{M|Ulfrun's Endurance}}
| {{Faction|Steel Meridian}}<br />{{Faction|Red Veil}}
|-
| {{WF|Wisp}}
| {{M|Fused Reservoir}} {{M|Critical Surge}} {{M|Cataclysmic Gate}}
| {{Faction|Cephalon Suda}}<br />{{Faction|New Loka}}
|-
| {{WF|Wukong}}
| {{M|Celestial Stomp}} {{M|Enveloping Cloud}} {{M|Primal Rage}}
| {{Faction|Arbiters of Hexis}}<br />{{Faction|New Loka}}
|-
| {{WF|Xaku}}
| {{M|Vampiric Grasp}} {{M|The Relentless Lost}} {{M|Untime Rift}}
| {{Faction|Cephalon Suda}}<br />{{Faction|Steel Meridian}}
|-
| {{WF|Yareli}}
| {{M|Merulina Guardian}} {{M|Loyal Merulina}} {{M|Surging Blades}}
| {{Faction|Cephalon Suda}}<br />{{Faction|New Loka}}
|-
| {{WF|Zephyr}}
| {{M|Target Fixation}} {{M|Airburst Rounds}} {{M|Jet Stream}} {{M|Funnel Clouds}} {{M|Anchored Glide}}
| {{Faction|Red Veil}}<br />{{Faction|New Loka}}
|-
|}
"""