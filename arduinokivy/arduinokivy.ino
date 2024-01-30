int normal1 = 38;  //38
int normal2 = 36;  //36
int normal3 = 34;  //34
int normal4 = 32;  //32
int normal5 = 30;  //30
int normal6 = 28;  //28
int normal7 = 26;  //26

int peking1 = 41;  //53
int peking2 = 43;  //51
int peking3 = 45;  //49
int peking4 = 47;  //47
int peking5 = 49;  //45
int peking6 = 51;  //43
int peking7 = 53;  //41

int kenong1 = 39;  //39
int kenong2 = 37;  //37
int kenong3 = 35;  //35
int kenong5 = 33;  //33
int kenong6 = 31;  //31
int kenong7 = 29;  //29
int pinGong = 27;  //27

int kalnm0 = 0;
int kalpk0 = 0;
int kalkn0 = 0;
int kalgong = 0;

int normalpukul = 0;
int pekingpukul = 0;
int kenongpukul = 0;
int gongpukul = 0;

int kalnm = 0;
int kalpk = 0;
int kalkn = 0;
int pukulgongkal = 0;
int pukulgongkalindex = 0;


String data;
String data1;
String data2;
String notasi = "";
int panjangnotasi = 0;

int nmonitor = 0;
int pmonitor = 0;
int kmonitor = 0;
int gmonitor = 0;

int endkenong = 0;
int ketukankenong = 0;
int datakenong = 0;

int ketukangong = 0;

int defaultinterval = 500;
int interval = 500;
int touchtime = 90;

enum Mode {
  Player,
  Kalibrasi
};

enum Pilihan {
  play,
  pause,
  stop
};

Pilihan pilihan = stop;
Mode mode = Player;

int index = 0;


void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.println("ArduinoDevices");


  pinMode(normal1, OUTPUT);
  pinMode(normal2, OUTPUT);
  pinMode(normal3, OUTPUT);
  pinMode(normal4, OUTPUT);
  pinMode(normal5, OUTPUT);
  pinMode(normal6, OUTPUT);
  pinMode(normal7, OUTPUT);

  pinMode(peking1, OUTPUT);
  pinMode(peking2, OUTPUT);
  pinMode(peking3, OUTPUT);
  pinMode(peking4, OUTPUT);
  pinMode(peking5, OUTPUT);
  pinMode(peking6, OUTPUT);
  pinMode(peking7, OUTPUT);

  pinMode(kenong1, OUTPUT);
  pinMode(kenong2, OUTPUT);
  pinMode(kenong3, OUTPUT);
  pinMode(kenong5, OUTPUT);
  pinMode(kenong6, OUTPUT);
  pinMode(kenong7, OUTPUT);
  pinMode(pinGong, OUTPUT);

  digitalWrite(normal1, HIGH);
  digitalWrite(normal2, HIGH);
  digitalWrite(normal3, HIGH);
  digitalWrite(normal4, HIGH);
  digitalWrite(normal5, HIGH);
  digitalWrite(normal6, HIGH);
  digitalWrite(normal7, HIGH);

  digitalWrite(peking1, HIGH);
  digitalWrite(peking2, HIGH);
  digitalWrite(peking3, HIGH);
  digitalWrite(peking4, HIGH);
  digitalWrite(peking5, HIGH);
  digitalWrite(peking6, HIGH);
  digitalWrite(peking7, HIGH);

  digitalWrite(kenong1, HIGH);
  digitalWrite(kenong2, HIGH);
  digitalWrite(kenong3, HIGH);
  digitalWrite(kenong5, HIGH);
  digitalWrite(kenong6, HIGH);
  digitalWrite(kenong7, HIGH);
  digitalWrite(pinGong, HIGH);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (mode == Player) {
    player();
  } else if (mode == Kalibrasi) {
    kalibrasi();
  }
}

void resetpinkal() {
  kalnm = 0;
  kalpk = 0;
  kalkn = 0;
  pukulgongkal = 0;
}

void player() {
  if (pilihan == play) {


    normalandpeking();
    kenong();


    pukul();
    Serial.println("Playing:Note " + String(nmonitor) + ":" + String(nmonitor) + String(pmonitor) + String(datakenong) + String(gmonitor) + ":index:" + String(index));



    delay(touchtime);

    Serial.println("off");
    angkat();

    pkpukuldua();
    // delay(interval / 2 - touchtime);
    delay(0.32 * interval);

    ++index;
    stopper();

    perlambatan();



  } else if (pilihan == pause) {
    Serial.println("off");
    Serial.println("pause nih!");
    delay(interval);
  } else if (pilihan == stop) {
    Serial.println("off");
    Serial.println("stop nih!");
    delay(interval);
  }
}

void kalibrasi() {

  String pesankalnormal = String(kalnm0);
  String pesankalpeking = String(kalpk0);
  String pesankalkenong = String(kalkn0);
  String pesankalgong = String(kalgong);
  resetpinkal();
  // Normal
  if (kalnm0 == 1) {
    kalnm = normal1;
  } else if (kalnm0 == 2) {
    kalnm = normal2;
  } else if (kalnm0 == 3) {
    kalnm = normal3;
  } else if (kalnm0 == 4) {
    kalnm = normal4;
  } else if (kalnm0 == 5) {
    kalnm = normal5;
  } else if (kalnm0 == 6) {
    kalnm = normal6;
  } else if (kalnm0 == 7) {
    kalnm = normal7;
  }


  // Peking
  if (kalpk0 == 1) {
    kalpk = peking1;
  } else if (kalpk0 == 2) {
    kalpk = peking2;
  } else if (kalpk0 == 3) {
    kalpk = peking3;
  } else if (kalpk0 == 4) {
    kalpk = peking4;
  } else if (kalpk0 == 5) {
    kalpk = peking5;
  } else if (kalpk0 == 6) {
    kalpk = peking6;
  } else if (kalpk0 == 7) {
    kalpk = peking7;
  }


  // kenong
  if (kalkn0 == 1) {
    kalkn = kenong1;
  } else if (kalkn0 == 2) {
    kalkn = kenong2;
  } else if (kalkn0 == 3) {
    kalkn = kenong3;
  } else if (kalkn0 == 5) {
    kalkn = kenong5;
  } else if (kalkn0 == 6) {
    kalkn = kenong6;
  } else if (kalkn0 == 7) {
    kalkn = kenong7;
  }

  // gong
  ++pukulgongkalindex;
  if (pukulgongkalindex > 3) {
    if (kalgong == 1) {
      pukulgongkal = pinGong;
      pukulgongkalindex = 0;
    }
  } else {
    pukulgongkal = 0;
    pesankalgong = "0";
  }


  digitalWrite(kalnm, LOW);
  digitalWrite(kalpk, LOW);
  digitalWrite(kalkn, LOW);
  digitalWrite(pukulgongkal, LOW);

  Serial.println(String("cal:") + pesankalnormal + pesankalpeking + pesankalkenong + pesankalgong);
  delay(touchtime);

  Serial.println("off");
  digitalWrite(kalnm, HIGH);
  digitalWrite(kalpk, HIGH);
  digitalWrite(kalkn, HIGH);
  digitalWrite(pukulgongkal, HIGH);

  delay(interval / 2 - touchtime);
  digitalWrite(kalpk, LOW);
  delay(touchtime);
  digitalWrite(kalpk, HIGH);

  delay(interval / 2 - touchtime);

  // delay(interval);
}

void perlambatan() {
  if (index == panjangnotasi - 8) {
    interval = defaultinterval * 1.5;
  } else if (index == panjangnotasi - 7) {
    interval = defaultinterval * 2;
  } else if (index == panjangnotasi - 6) {
    interval = defaultinterval * 2.25;
  } else if (index == panjangnotasi - 5) {
    interval = defaultinterval * 2.2;
  } else if (index == panjangnotasi - 4) {
    interval = defaultinterval * 3;
  }
}

void stopper() {
  if (index >= panjangnotasi) {
    pilihan = stop;
    notasi = "";
    index = 0;
    endkenong = 0;
    ketukankenong = 0;
    ketukangong = 0;
    interval = defaultinterval;
    Serial.println("finish");
  }
}

void normalandpeking() {
  int note = String(notasi[index]).toInt();
  if (zerocheck() == false) {
    if (note == 1) {
      nmonitor = 1;
      pmonitor = 1;
      normalpukul = normal1;
      pekingpukul = peking1;
    } else if (note == 2) {
      nmonitor = 2;
      pmonitor = 2;
      normalpukul = normal2;
      pekingpukul = peking2;
    } else if (note == 3) {
      nmonitor = 3;
      pmonitor = 3;
      normalpukul = normal3;
      pekingpukul = peking3;
    } else if (note == 4) {
      nmonitor = 4;
      pmonitor = 4;
      normalpukul = normal4;
      pekingpukul = peking4;
    } else if (note == 5) {
      nmonitor = 5;
      pmonitor = 5;
      normalpukul = normal5;
      pekingpukul = peking5;
    } else if (note == 6) {
      nmonitor = 6;
      pmonitor = 6;
      normalpukul = normal6;
      pekingpukul = peking6;
    } else if (note == 7) {
      nmonitor = 7;
      pmonitor = 7;
      normalpukul = normal7;
      pekingpukul = peking7;
    }
  } else {
    pmonitor = 0;
    nmonitor = 0;
    normalpukul = 0;
    pekingpukul = 0;
  }
}

void kenong() {
  int note = String(notasi[index + 3]).toInt();

  if (endkenong <= 0) {
    if (note == 1) {
      kmonitor = 1;
      kenongpukul = kenong1;
    } else if (note == 2) {
      kmonitor = 2;
      kenongpukul = kenong2;
    } else if (note == 3) {
      kmonitor = 3;
      kenongpukul = kenong3;
    } else if (note == 4) {
      kmonitor = 5;
      kenongpukul = kenong5;
    } else if (note == 5) {
      kmonitor = 5;
      kenongpukul = kenong5;
    } else if (note == 6) {
      kmonitor = 6;
      kenongpukul = kenong6;
    } else if (note == 7) {
      kmonitor = 7;
      kenongpukul = kenong7;
    } else if (note == 0) {
      kmonitor = 0;
      kenongpukul = 0;
    }
  }
  ++endkenong;
  if (endkenong > 3) {
    endkenong = 0;
  }
}

bool zerocheck() {
  int checker = String(notasi[index]).toInt();
  if (checker == 0) {
    return true;
  } else {
    return false;
  }
}

void pukulkenong() {

  ++ketukankenong;
  if (ketukankenong >= 2) {
    if (zerocheck() == false) {
      datakenong = kmonitor;
      digitalWrite(kenongpukul, LOW);
    }
    // Serial.println("if kenong");
    ketukankenong = 0;
  } else {
    // ketukankenong = 0;
    // Serial.println("else kenong");
    datakenong = 0;
  }
}

void pukulgong() {

  ++ketukangong;
  if (ketukangong >= 8) {
    if (zerocheck() == false) {
      gmonitor = 1;
      gongpukul = pinGong;
      digitalWrite(gongpukul, LOW);
    }
    ketukangong = 0;
  } else {
    gmonitor = 0;
    gongpukul = 0;
  }
}

void pukul() {
  digitalWrite(normalpukul, LOW);
  digitalWrite(pekingpukul, LOW);
  pukulkenong();
  pukulgong();
}

void angkat() {
  digitalWrite(normalpukul, HIGH);
  digitalWrite(pekingpukul, HIGH);
  digitalWrite(kenongpukul, HIGH);
  digitalWrite(gongpukul, HIGH);
}

void pkpukuldua() {
  if (index < panjangnotasi - 1) {
    delay(interval / 2 - touchtime);
    digitalWrite(pekingpukul, LOW);
    delay(touchtime);
    digitalWrite(pekingpukul, HIGH);
  }
}

void parsingData() {
  int indat1 = data.indexOf(':');
  int indat2 = data.indexOf(':', indat1 + 1);

  data1 = data.substring(0, indat1);
  data2 = data.substring(indat1 + 1, indat2);
}

void clearData() {
  data = "";
  data1 = "";
  data2 = "";
}

void reseter() {
  kalnm0 = 0;
  kalpk0 = 0;
  kalkn0 = 0;
  kalgong = 0;

  kalnm = 0;
  kalpk = 0;
  kalkn = 0;
  pukulgongkal = 0;
}

void menu() {
  if (data1 == "play") {
    pilihan = play;
    panjangnotasi = String(notasi).length();
    Serial.println("panjang notasi : " + String(panjangnotasi));
    Serial.println("Lagu di Play");
  } else if (data1 == "pause") {
    pilihan = pause;
    Serial.println("Lagu di Pause");
  } else if (data1 == "stop") {
    pilihan = stop;
    notasi = "";
    index = 0;
    endkenong = 0;
    ketukankenong = 0;
    ketukangong = 0;
    interval = defaultinterval;
    Serial.println("Lagu di Stop");
  } else if (data1 == "lanjut") {
    pilihan = play;
  } else if (data1 == "kecepatan") {
    defaultinterval = data2.toInt();
    interval = defaultinterval;
  } else if (data1 == "touchtime") {
    touchtime = data2.toInt();
  } else if (data1 == "index") {
    index = String(data2).toInt();
  } else if (data1 == "notasi") {
    notasi += data2;
    // Serial.println(data2);
  } else if (data1 == "kalibrasi") {
    mode = Kalibrasi;
  } else if (data1 == "player") {
    mode = Player;
  } else if (data1 == "normal1") {
    if (kalnm0 == 0) {
      kalnm0 = 1;
    } else {
      kalnm0 = 0;
    }
  } else if (data1 == "normal2") {
    if (kalnm0 == 0) {
      kalnm0 = 2;
    } else {
      kalnm0 = 0;
    }
  } else if (data1 == "normal3") {
    if (kalnm0 == 0) {
      kalnm0 = 3;
    } else {
      kalnm0 = 0;
    }
  } else if (data1 == "normal4") {
    if (kalnm0 == 0) {
      kalnm0 = 4;
    } else {
      kalnm0 = 0;
    }
  } else if (data1 == "normal5") {
    if (kalnm0 == 0) {
      kalnm0 = 5;
    } else {
      kalnm0 = 0;
    }
  } else if (data1 == "normal6") {
    if (kalnm0 == 0) {
      kalnm0 = 6;
    } else {
      kalnm0 = 0;
    }
  } else if (data1 == "normal7") {
    if (kalnm0 == 0) {
      kalnm0 = 7;
    } else {
      kalnm0 = 0;
    }
  } else if (data1 == "peking1") {
    if (kalpk0 == 0) {
      kalpk0 = 1;
    } else {
      kalpk0 = 1;
    }
  } else if (data1 == "peking2") {
    if (kalpk0 == 0) {
      kalpk0 = 2;
    } else {
      kalpk0 = 0;
    }
  } else if (data1 == "peking3") {
    if (kalpk0 == 0) {
      kalpk0 = 3;
    } else {
      kalpk0 = 0;
    }
  } else if (data1 == "peking4") {
    if (kalpk0 == 0) {
      kalpk0 = 4;
    } else {
      kalpk0 = 0;
    }
  } else if (data1 == "peking5") {
    if (kalpk0 == 0) {
      kalpk0 = 5;
    } else {
      kalpk0 = 0;
    }
  } else if (data1 == "peking6") {
    if (kalpk0 == 0) {
      kalpk0 = 6;
    } else {
      kalpk0 = 0;
    }
  } else if (data1 == "peking7") {
    if (kalpk0 == 0) {
      kalpk0 = 7;
    } else {
      kalpk0 = 0;
    }
  } else if (data1 == "kenong1") {
    if (kalkn0 == 0) {
      kalkn0 = 1;
    } else {
      kalkn0 = 0;
    }
  } else if (data1 == "kenong2") {
    if (kalkn0 == 0) {
      kalkn0 = 2;
    } else {
      kalkn0 = 0;
    }
  } else if (data1 == "kenong3") {
    if (kalkn0 == 0) {
      kalkn0 = 3;
    } else {
      kalkn0 = 0;
    }
  } else if (data1 == "kenong5") {
    if (kalkn0 == 0) {
      kalkn0 = 5;
    } else {
      kalkn0 = 0;
    }
  } else if (data1 == "kenong6") {
    if (kalkn0 == 0) {
      kalkn0 = 6;
    } else {
      kalkn0 = 0;
    }
  } else if (data1 == "kenong7") {
    if (kalkn0 == 0) {
      kalkn0 = 7;
    } else {
      kalkn0 = 0;
    }
  } else if (data1 == "gong") {
    if (kalgong == 0) {
      kalgong = 1;
    } else {
      kalgong = 0;
    }
  } else if (data1 == "reseter") {
    reseter();
  } else if (data1 == "switchnormal") {
    kalnm0 = 0;
  } else if (data1 == "switchpeking") {
    kalpk0 = 0;
  } else if (data1 == "switchkenong") {
    kalkn0 = 0;
  }
}

void serialEvent() {
  if (Serial.available()) {
    data = Serial.readString();

    parsingData();
    menu();
    Serial.println("done");


    clearData();
  }
}