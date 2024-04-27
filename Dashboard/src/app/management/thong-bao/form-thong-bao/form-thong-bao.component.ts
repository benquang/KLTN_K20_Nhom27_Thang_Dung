import { HttpEventType } from '@angular/common/http';
import { AfterViewInit, Component, EventEmitter, Input, OnInit, Output, TemplateRef } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { SystemConstant } from '@constants/system.constant';
import langDataEn from '@languages/en.json';
import langDataVi from '@languages/vi.json';
import { MakeForm } from '@models/common/make-form.model';
import { ModalData } from '@models/common/modal-data.model';
import { IThongBao, IThongBaoDTO } from '@models/management/thong-bao.model';
import { FileService } from '@services/common/file.service';
import { FormValidatorService } from '@services/common/form-validator.service';
import { ThongBaoService } from '@services/management/thong-bao.service';
import { NzModalRef, NzModalService } from 'ng-zorro-antd/modal';
import { NgxSpinnerService } from 'ngx-spinner';
import { ToastrService } from 'ngx-toastr';
import { timer } from 'rxjs';
import Editor from 'src/assets/libs/ckeditor5/build/ckeditor';

@Component({
  selector: 'app-form-thong-bao',
  templateUrl: './form-thong-bao.component.html',
  styleUrls: ['./form-thong-bao.component.scss'],
})
export class FormThongBaoComponent implements OnInit, AfterViewInit {
  @Input() modalData!: ModalData<IThongBao>;
  @Output() closeModal = new EventEmitter<boolean>();

  // Ngon ngu hien thi //////////
  langData: Record<string, string> = (localStorage.getItem('language') === 'en' ? langDataEn : langDataVi)
    .MNG.THONG_BAO;
  //////////////////////////////

  showCke = false;
  editor = Editor;
  cfgEditor = SystemConstant.CkEditorCfg;
  modalRef!: NzModalRef;
  bannerRatio = 885 / 590;
  preBannerImg: Blob | null = null;
  isChangedImage = false;

  form!: FormGroup<MakeForm<IThongBaoDTO>>;

  isFieldValid = this.formValidatorSvc.isFieldValid;
  displayFieldCssZorro = this.formValidatorSvc.displayFieldCssZorro;

  constructor(
    private thongBaoSvc: ThongBaoService,
    private fb: FormBuilder,
    private formValidatorSvc: FormValidatorService,
    private alert: ToastrService,
    private spinner: NgxSpinnerService,
    private nzModalSvc: NzModalService,
    private fileSvc: FileService,
  ) { }

  ngOnInit(): void {
    this.createForm();
  }

  ngAfterViewInit(): void {
    timer(250).subscribe(() => this.showCke = true);
  }

  createForm(): void {
    this.form = this.fb.nonNullable.group({
      tieuDe: ['', [Validators.required]],
      anhBiaId: ['', [Validators.required]],
      loaiThongBaoId: ['', [Validators.required]],
      noiDung: ['', [Validators.required]],
    });
    if (this.modalData.action === SystemConstant.ACTION.EDIT) {
      this.form.patchValue({
        tieuDe: this.modalData.data.tieuDe,
        anhBiaId: this.modalData.data.anhBiaId,
        loaiThongBaoId: this.modalData.data.loaiThongBaoId,
        noiDung: this.modalData.data.noiDung,
      });
    }
  }

  onCancel(): void {
    this.closeModal.emit(false);
  }

  onSubmit(): void {
    console.log(this.form.value);

    // Tạm thời turn off Validate cho field anhBiaId
    this.form.get('anhBiaId')?.setValidators(null);
    this.form.get('anhBiaId')?.updateValueAndValidity();
    // Nếu form valid thì đi tiếp
    if (this.form.valid) {
      // Upload preBannerImg nếu có đổi ảnh mới
      if (this.isChangedImage && this.preBannerImg) {
        this.spinner.show();
        const fileBanner = this.fileSvc.blobToFile(this.preBannerImg, `anh-bia-${Date.now()}.jpg`);
        this.fileSvc.uploadFile(fileBanner, 'anh-bia').subscribe({
          next: (uploadRes) => {
            if (uploadRes.type === HttpEventType.Response) {
              // Set ID banner vào form
              this.form.get('anhBiaId')?.setValue(uploadRes.body?.id ?? '');
              // Call api
              this.callApi();
            }
          },
        });
      } else {
        this.callApi();
      }
    } else {
      // Nếu form invalid thì turn on Validate cho field anhBiaId và validateAllFormFields
      this.form.get('anhBiaId')?.setValidators([Validators.required]);
      this.form.get('anhBiaId')?.updateValueAndValidity();
      this.formValidatorSvc.validateAllFormFields(this.form);
    }
  }

  callApi() {
    if (this.modalData.action === SystemConstant.ACTION.EDIT) {
      this.thongBaoSvc.update(this.form.value, this.modalData.data.id)
        .subscribe({
          next: () => {
            this.closeModal.emit(true);
            this.alert.success(this.langData.CAP_NHAT_THANH_CONG);
          },
        });
    } else {
      this.thongBaoSvc.create(this.form.value)
        .subscribe({
          next: () => {
            this.closeModal.emit(true);
            this.alert.success(this.langData.THEM_MOI_THANH_CONG);
          },
        });
    }
  }

  openCropImgModal(tpl: TemplateRef<unknown>) {
    this.modalRef = this.nzModalSvc.create({
      nzTitle: this.langData.CHUAN_HOA_HINH_ANH,
      nzContent: tpl,
      nzWidth: 700,
      nzFooter: null,
    });
  }
  closeCropImgModal(img: Blob | null) {
    if (img) {
      this.preBannerImg = img;
      this.isChangedImage = true;
    }
    this.modalRef.close();
  }
}
