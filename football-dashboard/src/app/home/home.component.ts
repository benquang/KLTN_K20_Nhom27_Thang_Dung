import { Component } from '@angular/core';
import { Meta } from '@angular/platform-browser';
import { CsvReaderService } from './csv-reader.service';

import { ActivatedRoute } from '@angular/router';
@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrl: './home.component.scss'
})
export class HomeComponent {

  constructor(
    private metaSvc: Meta,
    
    private csvReader: CsvReaderService,
    private route: ActivatedRoute,
  ) { }

  csvData: any;
  premier: any;
  ligue: any;
  bundes: any;
  serie: any;
  laliga: any;

  csvData1: any;
  premier1: any;
  ligue1: any;
  bundes1: any;
  serie1: any;
  laliga1: any;

  returnImage(tag: string): string {
    return '/assets/img/logo/' + tag + '.png';
  }

  ngOnInit(): void {

    this.metaSvc.updateTag({
      name: 'description',
      content: 'Demo 123',
    });

    const csvFilePath = '/assets/View_BXH_All_Leagues.csv';
    this.csvReader.readCsvData(csvFilePath)
      .then(data => {
        this.csvData = data;

        this.premier = this.csvData.filter(item => item.League_Name === 'Premier League')
        this.ligue = this.csvData.filter(item => item.League_Name === 'Ligue 1')
        this.bundes = this.csvData.filter(item => item.League_Name === 'Fußball-Bundesliga')
        this.serie = this.csvData.filter(item => item.League_Name === 'Serie A')
        this.laliga = this.csvData.filter(item => item.League_Name === 'La Liga')

        console.log(this.premier);

      })
      .catch(error => {
        console.error('Error reading CSV file:', error);
      });

      const csvFilePath1 = '/assets/Top_20_Scores_All_Leagues.csv';
      this.csvReader.readCsvData(csvFilePath1)
        .then(data => {
          this.csvData1 = data;
  
          this.premier1 = this.csvData1.filter(item => item.League_Name === 'Premier League').slice(0, 10)
          this.ligue1 = this.csvData1.filter(item => item.League_Name === 'Ligue 1').slice(0, 10)
          this.bundes1 = this.csvData1.filter(item => item.League_Name === 'Fußball-Bundesliga').slice(0, 10)
          this.serie1 = this.csvData1.filter(item => item.League_Name === 'Serie A').slice(0, 10)
          this.laliga1 = this.csvData1.filter(item => item.League_Name === 'La Liga').slice(0, 10)
  
          console.log(this.premier1);
  
        })
        .catch(error => {
          console.error('Error reading CSV file:', error);
        });

  }


}
