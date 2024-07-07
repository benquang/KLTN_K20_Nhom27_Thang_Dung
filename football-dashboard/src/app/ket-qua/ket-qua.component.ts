import { Component } from '@angular/core';

import { CsvReaderService } from './csv-reader.service';
import { Meta } from '@angular/platform-browser';
import { ActivatedRoute } from '@angular/router';



@Component({
  selector: 'app-ket-qua',
  templateUrl: './ket-qua.component.html',
  styleUrl: './ket-qua.component.scss'
})
export class KetQuaComponent {

  league_name: any;
  season: any;
  csvData: any;
  dates: any;
  week: any;
  groupedData: any;

  csvData1: any;

  year: any;

  groupByMatchDate(date: any) {
    return this.csvData.filter(item => item.Full_Date === date);    
  }

  loadCsvData() {
    // Example method to reload CSV data
    this.csvReader.readCsvData('/assets/View_Ket_Qua.csv')
      .then(data => {
        this.csvData = data;
      })
      .catch(error => {
        console.error('Error reading CSV file:', error);
      });
  }

  getDayOfWeek(day: string): string {
    if (day === 'Sun') {
      return 'CN';
    } else if (day === 'Sat') {
      return 'Thứ 7';
    } else if (day === 'Fri') {
      return 'Thứ 6';
    } else if (day === 'Thu') {
      return 'Thứ 5';
    } else if (day === 'Wed') {
      return 'Thứ 4';
    } else if (day === 'Tue') {
      return 'Thứ 3';
    } else if (day === 'Mon') {
      return 'Thứ 2';
    } else {
      return day;
    }
  }

  returnImage(tag: string): string {
    return '/assets/img/logo/' + tag + '.png';
  }

  //https://second-chariot-420108.firebaseapp.com
  //http://localhost:4200/ket-qua/Premier%20League/2024

  returnHistoryMatch(tag: string): string {
    return 'https://second-chariot-420108.firebaseapp.com' + '/tran-dau/' + tag;
  }

  returnKetqua(tag: string): string {
    return 'https://second-chariot-420108.firebaseapp.com' + '/ket-qua/' + tag + '/' + this.year;
  }

  returnKetqua2(tag: string): string {
    return 'https://second-chariot-420108.firebaseapp.com' + '/ket-qua/' + this.league_name + '/' + tag;
  }

  returnSeason(tag: string): string {
    if (tag === '2024') {
      return '2023-2024';
    }
    if (tag === '2023') {
      return '2022-2023';
    }
    if (tag === '2022') {
      return '2021-2022';
    }
    if (tag === '2021') {
      return '2020-2021';
    }
    if (tag === '2020') {
      return '2019-2020';
    }
    return '2023-2024'
  }

  isDropdownOpen = false;
  isDropdownOpen1 = false;

  myFunction(): void {
    this.isDropdownOpen = !this.isDropdownOpen;
  }
  myFunction1(): void {
    this.isDropdownOpen1 = !this.isDropdownOpen1;
  }

  onClickOutside(event: MouseEvent): void {
    if (!(event.target instanceof Element) || !event.target.matches('.dropbtn')) {
      this.isDropdownOpen = false;
    }
  }

  constructor(
    private metaSvc: Meta,
    private csvReader: CsvReaderService,
    private route: ActivatedRoute,
  ) { }

  ngOnInit(): void {

    this.metaSvc.updateTag({
      name: 'description',
      content: 'Demo 123',
    });


    this.league_name = this.route.snapshot.paramMap.get('league');
    this.year = this.route.snapshot.paramMap.get('season');

    const csvFilePath = '/assets/View_Ket_Qua.csv';
    this.csvReader.readCsvData(csvFilePath)
      .then(data => {
        this.csvData = data.filter(item => item.League_Name === this.league_name);                          
        this.csvData = this.csvData.filter(item => item.Season === this.year);                          

        this.dates = this.csvData.map(item => item.Full_Date)
        .filter((value, index, self) => self.indexOf(value) === index);

        this.week = this.csvData.map(item => item.Match_Week)
        .filter((value, index, self) => self.indexOf(value) === index);

        //console.log(this.csvData[0]);
      })
      .catch(error => {
        console.error('Error reading CSV file:', error);
      });


      const csvFilePath1 = '/assets/View_BXH_All_Leagues.csv';
      this.csvReader.readCsvData(csvFilePath1)
        .then(data => {
          this.csvData1 = data.filter(item => item.League_Name === this.league_name);
  
  
          console.log(this.csvData1);
  
        })
        .catch(error => {
          console.error('Error reading CSV file:', error);
        });

  }

  description = 'Tôi đã hoạt động 2 năm trong lĩnh vực BĐS với sức trẻ'
  + ' căng đầy nhiệt huyết, '
  + 'đã giúp tư vấn thành công nhiều giao dịch BĐS'
  + 'cho khách hàng mua nhà và chủ nhà tại thị trường TP. Hồ Chí Minh.';
cards = [
  {
    imageSrc: '/assets/img/logo/Premier_League_Logo.png',
    title: 'Premier League',
    description: 'Premier League, English professional football (soccer) league established in 1992. The league, which comprises 20 clubs, superseded the first division of the English Football League (EFL) as the top level of football in England.',
  },
  {
    imageSrc: '/assets/img/logo/laliga.png',
    title: 'Laliga',
    description: 'The Liga Nacional de Fútbol Profesional (transl. National Professional Football League), also known as LALIGA (the abbreviation LFP was used until the 2015–16 season), is a sports association responsible for administering the two professional football leagues in Spain, the Primera and Segunda Divisions',
  },
  {
    imageSrc: '/assets/img/logo/seriea.svg',
    title: 'Seria',
    description: "The Serie A, officially known as Serie A TIM for sponsorship reasons, is a professional league competition for football clubs located at the top of the Italian football league system and the winners are awarded the scudetto and the Coppa Campioni d'Italia.",
  },
  {
    imageSrc: '/assets/img/logo/bundesliga.png',
    title: 'Bundesliga',
    description: 'The Introduction of the Bundesliga was the long-debated step of establishing a top-level association football league in Germany in 1963. The new league, the Bundesliga, played its first season in 1963–64 and continues to be the highest league in the country. Its introduction reduced the number of first division teams in Germany from 74 to 16 and finally eliminated the problem of the top-teams having to play uncompetitive teams in regional leagues.',
  },
  {
    imageSrc: '/assets/img/logo/ligue1.png',
    title: 'Ligue 1',
    description: 'Ligue 1, officially known as Ligue 1 Uber Eats for sponsorship reasons, is a French professional league for men`s association football clubs.',
  },
];

}
