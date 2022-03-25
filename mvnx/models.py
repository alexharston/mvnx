import numpy as np
import xml.etree.ElementTree as ET
from tqdm import tqdm
import h5py
import re


class MVNX:
    """
    The abstract parser object to run through the XML tree structure of the MVNX file format
    and extract the relevant information into dictionaries and numpy arrays. Super simple, needs
    refactoring at the moment.

    Can also be used as a command line tool.
    """

    def __init__(self, path, orientation=None, position=None, velocity=None, \
                 acceleration=None, angularVelocity=None, angularAcceleration=None, \
                 footContacts=None, sensorFreeAcceleration=None, sensorMagneticField=None, \
                 sensorOrientation=None, jointAngle=None, jointAngleXZY=None, jointAngleErgo=None, \
                 centerOfMass=None, mapping=None, sensors=None, segments=None, joints=None, \
                 root=None, mvn=None, comment=None, subject=None, version=None, build=None, label=None, \
                 frameRate=None, segmentCount=None, recordingDate=None, configuration=None, userScenario=None, \
                 securityCode=None, modality=None, time=None, index=None, timecode=None, ms=None):
        if orientation is None:
            self.orientation = []
        if position is None:
            self.position = []
        if velocity is None:
            self.velocity = []
        if acceleration is None:
            self.acceleration = []
        if angularVelocity is None:
            self.angularVelocity = []
        if angularAcceleration is None:
            self.angularAcceleration = []
        if footContacts is None:
            self.footContacts = []
        if sensorFreeAcceleration is None:
            self.sensorFreeAcceleration = []
        if sensorMagneticField is None:
            self.sensorMagneticField = []
        if sensorOrientation is None:
            self.sensorOrientation = []
        if jointAngle is None:
            self.jointAngle = []
        if jointAngleXZY is None:
            self.jointAngleXZY = []
        if jointAngleErgo is None:
            self.jointAngleErgo = []
        if centerOfMass is None:
            self.centerOfMass = []
        if sensors is None:
            self.sensors = []
        if segments is None:
            self.segments = {}
        if joints is None:
            self.joints = {}
        if mapping is None:
            self.mapping = {"orientation": 0,
                            "position": 1,
                            "velocity": 2,
                            "acceleration": 3,
                            "angularVelocity": 4,
                            "angularAcceleration": 5,
                            "footContacts": 6,
                            "sensorFreeAcceleration": 7,
                            "sensorMagneticField": 8,
                            "sensorOrientation": 9,
                            "jointAngle": 10,
                            "jointAngleXZY": 11,
                            "jointAngleErgo": 12,
                            "centerOfMass": 13}
        if time is None:
            self.time = []
        else:
            self.time = time
        if index is None:
            self.index = []
        else:
            self.index = index
        if timecode is None:
            self.timecode = []
        else:
            self.timecode = timecode
        if ms is None:
            self.ms = []
        else:
            self.ms = ms
        self.mvn = mvn
        self.comment = comment
        self.subject = subject
        self.version = version
        self.build = build
        self.label = label
        self.subject = subject
        self.frameRate = frameRate
        self.segmentCount = segmentCount
        self.recordingDate = recordingDate
        self.configuration = configuration
        self.userScenario = userScenario
        self.securityCode = securityCode
        self.modality = modality
        if path is None:
            print('Please supply a path')
        self.path = path
        if root is None:
            self.parse_mvnx(self.path)
            self.parse_all()
        else:
            self.root = root

    def __repr__(self):
        return f'<MVNX ({self.path})>'

    def namespace(self, element):
        m = re.match(r'\{.*\}', element.tag)
        return m.group(0) if m else ''

    def parse_mvnx(self, path):
        """
        Take a path to an MVNX file and parse it

        Args:
            path ([string]): [the path to the data file]
        """
        tree = ET.parse(path)
        self.root = tree.getroot()
        self.ns = self.namespace(self.root)
        self.mvn = self.root.find(self.ns + 'mvn')
        # self.version = self.root[0].attrib['version']
        self.version = self.mvn.attrib['version']
        # self.build = self.root[0].attrib['build']
        self.build = self.mvn.attrib['build']
        #self.comment = self.root[1].text
        self.comment = self.root.find(self.ns + 'comment').text
        #self.label = self.root[2].attrib['label']
        self.subject = self.root.find(self.ns + 'subject')
        self.label = self.subject.attrib['label']
        self.frameRate = self.subject.attrib['frameRate']
        self.frameRate_ = self.subject.attrib['frameRate']
        self.segmentCount = self.subject.attrib['segmentCount']
        self.recordingDate = self.subject.attrib['recDate']
        try:
            self.configuration = self.subject.attrib['configuration']
        except:
            print("No configuration for subject provided. Using FullBody as default.")
            self.configuration = "FullBody"
        try:
            self.userScenario = self.subject.attrib['userScenario']
        except:
            print("No user scenarios for subject provided. Using multiLevel as default.")
            self.configuration = "multiLevel"

        self.securityCode = self.root.find(self.ns + 'securityCode').attrib['code']
        return self.root

    def parse_modality(self, modality):

        """[With a given XML Tree, parse out the salient modalities within each frame]

        Args:

            modality ([string]): [the name of the modality]

        """

        holding_list = []
        #frames = self.root[2][6]
        frames = self.subject.find(self.ns + 'frames')
        for frame in tqdm(frames[3:]):
            for child in frame[self.mapping[modality]:self.mapping[modality] + 1]:
                holding_list.append(child.text.split(' '))
        holding_list = np.array(holding_list)
        try:
            holding_list = holding_list.astype(float)
        except:
            print("Ignoring element, since it's not a floatable value")
            return None
        return holding_list.astype(float)

    def parse_time(self):
        frames = self.subject.find(self.ns + 'frames')[3:]
        for frame in tqdm(frames):
            self.time.append(frame.attrib['time'])
        return self.time

    def parse_index(self):
        frames = self.subject.find(self.ns + 'frames')[3:]
        for frame in tqdm(frames):
            self.index.append(frame.attrib['index'])
        return self.index

    def parse_timecode(self):
        frames = self.subject.find(self.ns + 'frames')[3:]
        for frame in tqdm(frames):
            if 'tc' in  frame.attrib:
                self.timecode.append(frame.attrib['tc'])
            else:
                self.timecode.append('')
        return self.timecode

    def parse_ms(self):
        frames = self.subject.find(self.ns + 'frames')[3:]
        for frame in tqdm(frames):
            if 'mc' in frame.attrib:
                self.ms.append(frame.attrib['ms'])
            else:
                self.ms.append('')
        return self.ms

    def parse_modalities(self, *args):
        for arg in tqdm(args):
            print(self.parse_modality(arg))
            return self.parse_modality(arg)

    def parse_sensors(self):
        #sensors = self.root[2][2]

        sensors =  self.subject.find(self.ns + 'sensors')
        if sensors:

            for sensor in tqdm(self.root[2][2]):
                self.sensors.append(sensor.attrib['label'])
            return self.sensors
        else:
            return None

    def parse_segments(self):
        #segments = self.root[2][1]

        segments = self.subject.find(self.ns + 'segments')

        if segments:
            for segment in tqdm(segments):
                self.segments[segment.attrib['id']] = segment.attrib['label']
            return self.segments
        else:
            return None

    def parse_joints(self):

        #joints = self.root[2][3]

        joints = self.subject.find(self.ns + 'joints')

        if joints:
            for joint in tqdm(joints):
                self.joints[joint.attrib['label']] = [joint[0].text, joint[1].text]
            return self.joints
        else:
            return None

    def parse_all(self):
        for key in tqdm(self.mapping.keys()):
            setattr(self, key, self.parse_modality(key))
        self.parse_time()
        self.parse_joints()
        self.parse_segments()
        self.parse_sensors()
        self.parse_timecode()
        self.parse_ms()

    def save_to_HDF5(self, filepath):
        """Create an HDF5 file from an MVNX object.

        :param filepath: _description_ - the path to the file you want to create
        :type filepath: _type_
        """
        with h5py.File(f'{filepath}.hdf5', 'w') as f:
            jointAngle = f.create_dataset("jointAngle", data=self.jointAngle)
            jointAngleXZY = f.create_dataset("jointAngleXZY", data=self.jointAngleXZY)
            angularVelocity = f.create_dataset("angularVelocity", data=self.angularVelocity)
            angularAcceleration = f.create_dataset("angularAcceleration", data=self.angularAcceleration)
            position = f.create_dataset("position", data=self.position)
            orientation = f.create_dataset("orientation", data=self.orientation)
            centerOfMass = f.create_dataset("centerOfMass", data=self.centerOfMass)
