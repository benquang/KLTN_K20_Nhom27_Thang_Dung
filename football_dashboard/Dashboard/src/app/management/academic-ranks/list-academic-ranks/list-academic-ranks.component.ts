import { Component, OnInit, TemplateRef } from '@angular/core';
import { SystemConstant } from '@constants/system.constant';
import { UrlConstant } from '@constants/url.constant';
import langDataEn from '@languages/en.json';
import langDataVi from '@languages/vi.json';
import { ModalData } from '@models/common/modal-data.model';
import { UntilDestroy } from '@ngneat/until-destroy';
import { BreadCrumb } from '@widget/breadcrumb/breadcrumb.model';
import { Paginate } from '@widget/paginate/paginate.model';
import { NzModalService } from 'ng-zorro-antd/modal';
import { NgxSpinnerService } from 'ngx-spinner';
import { ToastrService } from 'ngx-toastr';
import { IAcademicRanks } from '../DEMO-academic.model';
import { AcademicRanksService } from '../DEMO-academic.service';

@UntilDestroy()
@Component({
  selector: 'app-list-academic-ranks',
  templateUrl: './list-academic-ranks.component.html',
  styleUrls: ['./list-academic-ranks.component.scss'],
})
export class ListAcademicRanksComponent implements OnInit {

  // Ngon ngu hien thi //////////
  langCode: 'en' | 'vi' = localStorage.getItem('language') as 'en' | 'vi' ?? 'vi';
  langData: Record<string, string> = (localStorage.getItem('language') === 'en' ? langDataEn : langDataVi)
    .MNG.CATEGORIES.ACADEMIC_RANKS;
  //////////////////////////////

  breadcrumbObj: BreadCrumb = new BreadCrumb({
    heading: this.langData.HOC_HAM,
    listBreadcrumb: [{
      title: this.langData.DANH_MUC,
      link: UrlConstant.ROUTE.MANAGEMENT.CATEGORIES,
    }],
  });

  listAcademicRanks = new Paginate<IAcademicRanks>();
  modalData = new ModalData<IAcademicRanks>();
  searchValue = '';
  selectedSwitcherId = '';

  constructor(
    private spinner: NgxSpinnerService,
    private alert: ToastrService,
    private nzModalSvc: NzModalService,
    private academicRanksSvc: AcademicRanksService,
  ) { }

  ngOnInit(): void {
    this.getDataPaging();
  }

  getDataPaging(isSearch?: boolean): void {
    if (isSearch) {
      this.listAcademicRanks.currentPage = 1;
    }
    this.spinner.show();
    this.academicRanksSvc.getAllPaging(
      this.listAcademicRanks.currentPage - 1,
      this.listAcademicRanks.limit,
      this.searchValue)
      .subscribe({
        next: res => {
          this.listAcademicRanks.currentPage = res.pageable.pageNumber + 1;
          this.listAcademicRanks.limit = res.pageable.pageSize;
          this.listAcademicRanks.totalPage = res.totalPages;
          this.listAcademicRanks.totalItem = res.totalElements;
          this.listAcademicRanks.data = res.content;
        },
      });
  }

  trackByFn = (_index: number, data: IAcademicRanks) => data.id;

  openModal(template: TemplateRef<unknown>, data?: IAcademicRanks): void {
    if (data) {
      this.modalData.action = SystemConstant.ACTION.EDIT;
      this.modalData.data = data;
    } else {
      this.modalData.action = SystemConstant.ACTION.ADD;
    }
    this.nzModalSvc.create({
      nzStyle: { top: '20px' },
      nzWidth: 500,
      nzTitle: `${(data ? this.langData.CHINH_SUA :
        this.langData.THEM_MOI)} ${this.breadcrumbObj.heading}`,
      nzContent: template,
      nzFooter: null,
      nzMaskClosable: false,
    });
  }

  closeModal(reload?: boolean): void {
    if (reload) {
      this.getDataPaging();
    }
    this.nzModalSvc.closeAll();
  }

  pageChange(page: Paginate<IAcademicRanks>): void {
    this.listAcademicRanks = page;
    this.getDataPaging();
  }

  changeStatus(id: string): void {
    this.selectedSwitcherId = id;
    this.nzModalSvc.confirm({
      nzWidth: 300,
      nzTitle: this.langData.XAC_NHAN_THAY_DOI_TRANG_THAI,
      nzCancelText: this.langData.HUY,
      nzOkDanger: true,
      nzOkText: this.langData.XAC_NHAN,
      nzOnOk: () => {
        this.spinner.show();
        this.academicRanksSvc.delete(id)
          .subscribe({
            next: () => {
              this.alert.success(this.langData.THAY_DOI_THANH_CONG);
              this.getDataPaging();
              this.selectedSwitcherId = '';
            },
            error: () => this.selectedSwitcherId = '',
          });
      },
      nzOnCancel: () => this.selectedSwitcherId = '',
    });
  }
}
