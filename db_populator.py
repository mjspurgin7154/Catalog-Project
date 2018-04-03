#!/usr/bin/env python
# -*- coding: utf-
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_setup import Base, Category, Item, User
from random import randint
import datetime
import random

engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

master_list = [
    ('Appliances',
        'Refrigerators',
            'A refrigerator is a popular household appliance that consists of a thermally insulated compartment and a heat pump (mechanical, electronic or chemical) that transfers heat from the inside of the fridge to its external environment so that the inside of the fridge is cooled to a temperature below the ambient temperature of the room.',
        'Microwaves',
            'A microwave oven is a kitchen appliancethat heats and cooks food by exposing it to electromagnetic radiation in the microwave frequency range. This induces polar molecules in the food to rotate and produce thermal energy in a process known as dielectric heating.'
    ),
    ('Bath',
        'Faucets',
            'A faucet is a valve controlling the release of water in a sink or shower',
        'Sinks',
            'A sink is a bowl-shaped plumbing fixture used for washing hands, dishwashing, and other purposes'
    ),
    ('Building Materials',
        'Lumber',
            'Lumber is a type of wood that has been processed into beams and planks, a stage in the process of wood production',
        'Siding',
            'Siding is the protective material attached to the exterior side of a wall of a house or other building'
    ),
    ('Electrical',
        'Wire',
            'A wire is a single, usually cylindrical, flexible strand or rod of metal. Wires are used to carry electricity and telecommunications signals.',
        'Conduit',
            'An electrical conduit is a tube used to protect and route  electrical wiring in a building or structure.'
    ),
    ('Hardware',
        'Screws',
            'A screw is a type of fastener, sometimes similar to a bolt, typically made of metal, and characterized by a helical ridge, known as a male thread (external thread) or just thread.',
        'Nails',
            'In woodworking and construction, a nail is a pin-shaped object of metal which is used as a fastener, as a peg to hang something, or sometimes as a decoration.'
    ),
    ('Heating & Cooling',
        'Thermostats',
            'A thermostat is a component which senses the temperature of a  system so that the system\'s temperature is maintained near a desired setpoint.',
        'Heaters',
            'Heaters are appliances whose purpose is to generate heat (i.e. warmth) for the building. This can be done via central heating. Such a system contains a boiler, furnace, or heat pump to heat water, steam, or air in a central location such as a furnace room in a home, or a mechanical room in a large building. The heat can be transferred by convection, conduction, or radiation.'
    ),
    ('Kitchen',
        'Cabinets',
            'Kitchen cabinets are the built-in furniture installed in many kitchens for storage of food, cooking equipment, and often  silverware and dishes for table service. Appliances such as  refrigerators, dishwashers, and ovens are often integrated into kitchen cabinetry. There are many options for cabinets available at present.',
        'Countertops',
            'A countertop is a horizontal work surface in kitchens or other food preparation areas, bathrooms or lavatories, and workrooms in general. It is frequently installed upon and supported by cabinets.'
    ),
    ('Paint',
        'Paint',
            'Paint is any liquid, liquefiable, or mastic composition that, after application to a substratein a thin layer, converts to a  solid film. It is most commonly used to protect, color, or provide texture to objects.',
        'Stains',
            'A wood stain consists of colorants dissolved and/or suspended in a "vehicle" or solvent. Vehicle is the preferred term, as the contents of a stain may not be truly dissolved in the vehicle, but rather suspended, and thus the vehicle may not be a true solvent.'
            ),
    ('Plumbing',
        'Pipes',
            'A pipe is a tubular section or hollow cylinder, usually but not necessarily of circularcross-section, used mainly to convey substances which can flow such as liquids and gases (fluids), slurries, powders and masses of small solids.',
        'Valves',
            'A valve is a device that regulates, directs or controls the flow of a fluid (gases, liquids, fluidized solids, or slurries) by opening, closing, or partially obstructing various passageways.'
            ),
    ('Tools',
        'Power',
            'A power tool is a tool that is actuated by an additional power source and mechanism other than the solely manual labourused with hand tools. The most common types of power tools use electric motors. Internal combustion engines and compressed air are also commonly used.',
        'Hand',
            'A hand tool is any tool that is powered by hand rather than a motor.  Categories of hand tools include wrenches, pliers, cutters, striking tools, struck or hammered tools, screwdrivers, vises, clamps, snips, saws, drills and knives.'
    )
    ]

# Generate random dates
def CreateRandomDate():
    today = datetime.date.today()
    days_old = randint(0,540)
    dateadded = today - datetime.timedelta(days = days_old)
    return dateadded

# Load Categories into database


for i in master_list:
    category = Category(user_id = 1, name = i[0])
    item1 = Item(user_id = 1, name = i[1], desc = i[2], dateadded = CreateRandomDate(), category=category)
    item2 = Item(user_id = 1, name = i[3], desc = i[4], dateadded = CreateRandomDate(), category=category)
    session.add(category)
    session.add(item1)
    session.add(item2)
    session.commit()

user_list = [
    ('Michael Spurgin', 'mjspurgin7154@gmail.com')
    ]

for elem in user_list:
    newUser = User(name=elem[0], email=elem[1])
    session.add(newUser)
    session.commit()

print('Categories have been added')
print('Items have been added')
